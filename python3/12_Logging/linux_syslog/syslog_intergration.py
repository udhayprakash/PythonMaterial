import logging 
from logging.handlers import SysLogHandler

logger = logging.getLogger("My appy")
logger.setLevel(logging.DEBUG)

handler = SysLogHandler(address = '/dev/log')
logger.addHandler(handler)

logger.debug("Hello these are debug message")
logger.error("Hello these are error message")
