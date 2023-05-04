import sys

from loguru import logger

logger.add("file.log")
logger.add(sys.stderr, level="ERROR")

logger.info("This message will be logged to both file and stderr")
