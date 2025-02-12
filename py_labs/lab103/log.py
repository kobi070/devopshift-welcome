import logging
import os
import sys
import json

# Mock data
server_dictionary = {
    "nginx": True,
    "apache": False,
    "mysql": True,
    "postgresql": False,
    "mongodb": False,
    "docker": False,
}

log_level = os.environ.get("LOG_LEVEL", "DEBUG")
log_format = os.environ.get("LOG_FORMAT", "JSON")

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        json_log = {
            "time": record.created,
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
        }
        return json.dumps(json_log)



"""
    logger = logging.getLogger named kobi
    logger level is set to log_level
    stdout handler uses JSONFormatter
    handler has two handlers, one for stdout and one for file
    file handler logs to logs.json
"""
def setup_logging():
    logger = logging.getLogger("myapp_logger")
    logger.setLevel(log_level)

    file_name = f"logs.{log_format.lower()}"
    steam_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(file_name)

    if(log_format == "JSON"):
        json_forrmater = JSONFormatter()
        file_handler.setFormatter(json_forrmater)
        steam_handler.setFormatter(json_forrmater)
    else:
        log_formmater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        steam_handler.setFormatter(log_formmater)

    logger.addHandler(steam_handler)
    logger.addHandler(file_handler)
    return logger

