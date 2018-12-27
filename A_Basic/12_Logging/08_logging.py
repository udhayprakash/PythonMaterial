#!/usr/bin/python
# fourth.py
import logging as l  # alias import

# creating a handler
han = l.FileHandler('08_logging.log')

# Formatter
formatting = l.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

# adding the formate to the handle
han.setFormatter(formatting)

# starting of logger
logger = l.getLogger('udhayApp')
# adding the handle to the logger
logger.addHandler(han)

# setting the level for logs.
logmessage = "testing the log messages"
logger.error(logmessage)
