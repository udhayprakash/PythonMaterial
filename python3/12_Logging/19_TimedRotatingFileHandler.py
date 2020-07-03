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

log_file_name = os.path.join('logs', os.path.splitext(__file__)[0] + '.log')
handler = TimedRotatingFileHandler(log_file_name,
                                   when="S",  # Seconds
                                   interval=5,
                                   backupCount=5)

handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(30):
    logger.info(f"This is log number: {i:2}")
    time.sleep(1)
