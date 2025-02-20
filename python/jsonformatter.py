import json

class JSONFormatter(logging.Formatter):
    # This is a class that will be used to format the logging messages
    # We will create a class that will inherit from the logging.Formatter class
    # We will create a format method that will take a record argument
    # We will create a log_record dictionary that will have the following keys:
    # timestamp, name, level, message
    # We will set the timestamp key to the current time
    # We will set the name key to the name attribute of the record argument
    # We will set the level key to the levelname attribute of the record argument
    # We will set the message key to the message attribute of the record argument
    # We will return the log_record dictionary as a JSON string
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "name": record.name,
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)