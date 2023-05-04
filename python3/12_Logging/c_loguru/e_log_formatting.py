import sys

from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}")

logger.info("This message will be logged with a custom format")

# adding color to log
logger.add(sys.stderr, colorize=True)

logger.info("<green>This message</green> will be logged in green")
