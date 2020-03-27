#!/usr/bin/python
"""
Purpose: Using Memory Handler
"""
import atexit
import logging.handlers
import os
import sys

LOG_LEVEL = logging.DEBUG

formatter = logging.Formatter('%(asctime)s - %(levelname)8s - %(message)s')

# Step 1: Create handlers
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(LOG_LEVEL)
stream_handler.setFormatter(formatter)

memory_handler = logging.handlers.MemoryHandler(
    capacity=1024 * 1,  # 1 kb
    flushLevel=logging.ERROR,
    target=stream_handler
)

file_handler = logging.FileHandler(os.path.splitext(__file__)[0] + '.log')
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(formatter)

# Step 2: Create logger object
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

# Step 3: Add handlers to the logger object
logger.addHandler(memory_handler)
logger.addHandler(file_handler)


def flush():
    memory_handler.flush()


atexit.register(flush)
loop_count = 0
while loop_count <= 100000:
    logger.debug(f'This is {loop_count:6} log')
    logger.info(f'This is {loop_count:6} log')
    logger.warning(f'This is {loop_count:6} log')
    logger.error(f'This is {loop_count:6} log')
    logger.critical(f'This is {loop_count:6} log')
    loop_count += 1

