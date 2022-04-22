#!/usr/bin/python
"""
Purpose: Rotating log handlers
"""
import logging
import os
from logging.handlers import RotatingFileHandler
from time import sleep

# print(dir(logging.handlers))

# # Method 1
# log_file_name = os.path.join('logs', os.path.splitext(__file__)[0] + '.log')
# logging.basicConfig(
#     handlers=[RotatingFileHandler(
#         log_file_name, maxBytes=1000, backupCount=2)],
#     level=logging.DEBUG,
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
#     datefmt='%Y-%m-%dT%H:%M:%S')

# for i in range(50):
#     logging.warning(f'Hello world!: {i:5}')
#     sleep(3)


# Method 2
logger = logging.getLogger("my_logger")
handler = RotatingFileHandler("logs/my_log.log", maxBytes=2000, backupCount=2)
logger.addHandler(handler)

for i in range(50):
    logger.warning(f"Hello world!: {i:5}")
    sleep(3)
