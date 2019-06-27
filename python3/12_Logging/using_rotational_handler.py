import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('my_logger')
handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=2)
logger.addHandler(handler)

for _ in range(10000):
    logger.warning('Hello, world!')