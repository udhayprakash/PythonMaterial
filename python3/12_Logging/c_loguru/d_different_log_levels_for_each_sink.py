import sys

from loguru import logger

logger.add("file.log", level="WARNING")
logger.add(sys.stderr, level="ERROR")

logger.debug("This message will not be logged")
logger.warning("This message will be logged to file only")
logger.error("This message will be logged to both file and stderr")
