#!/usr/bin/python
# fifth.py
import logging

'''
	Purpose: Demonstartion of logging
'''

# set my logger
logger = logging.getLogger('newApp')

# defining the handler
han = logging.FileHandler('newApp.log')

# Formatter
formate = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# creating the formatter for our handle
han.setFormatter(formate)

# Adding the handler to the logger. 
logger.addHandler(han)

logger.debug("Hello this is a debug message")
logger.info("Hello this is information")
logger.warning("Hello this is a warning")
logger.error("Hello this is an error")
logger.critical("Hello this an critical error\n")

logging.debug("Hello this is a debug message1")
logging.info("Hello this is information 1\n")
logging.warning("Hello this is a warning 1\n")
logging.error("Hello this is an error 1\n")
logging.critical("Hello this an critical error 1\n")


# It is different from logging.critical("Hello this an critical error")
