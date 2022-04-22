#!/usr/bin/python
"""
Purpose: Logging in JSON format

    pip install -U python-json-logger --user

"""
import logging

from pythonjsonlogger import jsonlogger

# Step 1: create handler
logHandler = logging.StreamHandler()

# Step 2: create json formatter
formatter = jsonlogger.JsonFormatter()

# Step 3: Add formatting to handler
logHandler.setFormatter(formatter)

# Step 4: create logger object
logger = logging.getLogger("myApp")

# Step 5: Add handler to the logger object
logger.addHandler(logHandler)
logger.setLevel(logging.DEBUG)

logger.debug("This is debug log")
logger.info("This is info log")
logger.warning("This is error log")
logger.error("This is error log")
logger.critical("This is critical log")


# Assignment: Add datetime & level to this
