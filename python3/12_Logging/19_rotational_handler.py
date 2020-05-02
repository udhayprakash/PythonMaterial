#!/usr/bin/python
"""
Purpose: Rotating log handlers
"""
import os
import logging
from logging.handlers import RotatingFileHandler
from time import sleep 

# Method 1
logging.basicConfig(
    handlers=[RotatingFileHandler(os.path.splitext(__file__)[0] + '.log',
                                  maxBytes=1000, backupCount=2)],
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt='%Y-%m-%dT%H:%M:%S')

for i in range(50):
    logging.warning(f'Hello world!: {i:5}')
    sleep(2)



# # Method 2
# logger = logging.getLogger('my_logger')
# handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=2)
# logger.addHandler(handler)

# for _ in range(100):
#     logger.warning('Hello, world!')
