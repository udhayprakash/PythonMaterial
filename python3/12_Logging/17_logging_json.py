import logging
import logging.config
import json


class JsonFormatter:
    ATTR_TO_JSON = [
        "created",
        "filename",
        "funcName",
        "levelname",
        "lineno",
        "module",
        "msecs",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "thread",
        "threadName",
    ]

    def format(self, record):
        obj = {attr: getattr(record, attr) for attr in self.ATTR_TO_JSON}
        return json.dumps(obj, indent=4)


console_handler = logging.StreamHandler()
console_handler.formatter = JsonFormatter()

file_handler = logging.FileHandler(filename="logs/17_logging_json.json", mode="w")
file_handler.formatter = JsonFormatter()

logger = logging.getLogger(__name__)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
