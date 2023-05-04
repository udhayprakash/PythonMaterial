import sys

from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}")
logger.info("This message will be logged with a custom format")
print()

# adding color to log
logger.add(sys.stderr, colorize=True)
logger.info("<green>This message</green> will be logged in green")
print()


# time formatting
logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}")
logger.info("This message will include a timestamp")
print()


# different timezone
import pytz

tz = pytz.timezone("Europe/Paris")

logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} {message}", serialize=False)
logger.bind(time=tz).info("This message will include the Paris timezone")
