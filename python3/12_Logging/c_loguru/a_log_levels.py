import sys

from loguru import logger

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
print()

# setting minimum level of severity
logger.add(sys.stdout, level="DEBUG")

logger.trace("This message has the lowest severity level")
logger.debug("This message has a low severity level")
logger.info("This message has a moderate severity level")
logger.warning("This message has a high severity level")
logger.error("This message has a very high severity level")
logger.critical("This message has the highest severity level")
print()


# Custom filters
def is_warning_or_error(record):
    return record["level"].name in ("WARNING", "ERROR")


logger.add(sys.stderr, filter=is_warning_or_error)

logger.info("This message will not be logged")
logger.warning("This message will be logged")
logger.error("This message will be logged")
