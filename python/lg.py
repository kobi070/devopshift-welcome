# logging is for debugging, infro and etc - Refernece: https://docs.python.org/3/library/logging.html
# os is for the operating system variables and etc - https://docs.python.org/3/library/os.html
# sys is for the python variables and etc - https://docs.python.org/3/library/sys.html
# Python library for json files - https://docs.python.org/3/library/json.html
import logging
import os
import sys
import json


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        json_log = {
            "time": record.asctime,
            "name": record.name,
            "module": record.module,
            "level": record.levelname,
            "message": record.msg,
            "format": record.getMessage()
        }
        return json.dumps(json_log)



"""
    # Prints of os and sys
    print(os.environ.keys()) # Prints of os environment variables keys
    print(sys.argv) # Prints of sys environment variables => in this case will print the name of this certain file
"""

"""
    Edit of the basic configuration of the logging => this works for every logger i will create as its a working on the logging config
    filename= where the logger is storeing the info and everything that bellow info in the hierarchy
    level= the level of the logging, in this case it is info
    format= the format of the logging, in this case it is a certain format string we created. 
    logging.basicConfig(filename="my_app.log") => example without enforcing all the loggers to use the lvl of INFO
    logging.basicConfig(filename="my_app.log", level=logging.INFO) => example with enforcing all the loggers to use the lvl of INFO
    We can create a log_format file which is a format string which will be used to format all the log messages
    log_format = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
    logging.basicConfig(filename="my_app.log", format=log_format)
"""

"""
    Creation of a basic logger named kobi
    Creating another logger named another_logger => set this certain logging settings with setLevel() to INFO
    logger2 = logging.getLogger("another_logger").setLevel(logging.INFO) => works the same
"""

logger = logging.getLogger("kobi")
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

"""
    Diffrent usage for logging modules (info, debug, warning, error, critical => by that order)
    The output will be printed to the console
    Can use setLevel() to set the logging level
"""
logger.setLevel(level=logging.INFO)
logger.info("This is a Info message")
logger.warning("This is a Warning message")
logger.debug("This is a Debug message")
logger.error("This is a Error message")

#  We will create the same for logger2
logger2 = logging.getLogger("another_logger")
logger2.setLevel(level=logging.DEBUG)
logger2.info("This is a Info message")
logger2.warning("This is a Warning message")
logger2.debug("This is a Debug message")
logger2.error("This is a Error message")

# logger.INFO => server is running, server is not running 
