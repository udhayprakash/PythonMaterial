#!/usr/bin/python
"""
Purpose: Time Rotational Handler
    S - Seconds
    M - Minutes
    H - Hours
    D - Days
    W0-w6 - weekday(0-Monday)
    midnight
"""
import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)8s - %(name)s - %(message)s')

handler = TimedRotatingFileHandler(os.path.splitext(__file__)[0] + '.log',
                                   when="S",  # Seconds
                                   interval=3,
                                   backupCount=5)

handler.setFormatter(formatter)
logger.addHandler(handler)

for _ in range(30):
    logger.info("This is a test!")
    time.sleep(1)
