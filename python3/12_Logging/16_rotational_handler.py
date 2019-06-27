import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
        handlers=[RotatingFileHandler('my_log.log', 
                      maxBytes=1000, backupCount=2)],
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')

for _ in range(10):
    logging.warning('Hello world!')

# logger = logging.getLogger('my_logger')
# handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=2)
# logger.addHandler(handler)

# for _ in range(10):
#     logger.warning('Hello, world!')