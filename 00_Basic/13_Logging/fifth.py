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

logger.debug("Hello this is a debug message \n")
logger.info("Hello this is information \n")
logger.warning("Hello this is a warning \n")
logger.error("Hello this is an error \n")
logger.critical("Hello this an critical error \n")

# It is different from logging.critical("Hello this an critical error \n")