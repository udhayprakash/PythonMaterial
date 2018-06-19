#!/usr/bin/python
# fourth.py
import logging as l  # alias import

# starting of logger
logger = l.getLogger()

# creating a handler

han = l.FileHandler('fourth.log')

# Formatter
format = l.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

# adding the formate to the handle
han.setFormatter(format)

# adding the handle to the logger
logger.addHandler(han)

# setting the level for logs.
logmessage = "testing the log messages"
l.error(logmessage)
