#!/usr/bin/python
"""
Purpose: To display the logs in console only

    step 1: create handler object and its config
    step 2: create logger objects and its config
    step 3: add the handler to logger object
    step 4: use the logger object for logging
"""
import logging

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)8s - %(name)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# creating you logger.
logger = logging.getLogger("myapp")  # 'logger' object was created
logger.setLevel(logging.DEBUG)

# add ch to logger
logger.addHandler(ch)


# 'application' code
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")

logging.critical("critical message2")
