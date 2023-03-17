#!/usr/bin/python
"""
Purpose: To display the logs in file only

    step 1: create handler object and its config
    step 2: create logger objects and its config
    step 3: add the handler to logger object
    step 4: use the logger object for logging
"""
import logging

# creating a handler
han = logging.FileHandler(filename="logs/13_logging.log")

# Formatter
formatting = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

# adding the format to the handle
han.setFormatter(formatting)

# starting of logger
logger = logging.getLogger("pythonApp")

# adding the handle to the logger
logger.addHandler(han)


# setting the level for logs.
logmessage = "testing the log messages"
logger.error(logmessage)


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.error(logmessage)
