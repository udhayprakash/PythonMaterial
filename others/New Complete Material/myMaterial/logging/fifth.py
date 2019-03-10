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

logging.debug("Hello this is a debug message \n")
logging.info("Hello this is information \n")
logging.warning("Hello this is a warning \n");
logging.error("Hello this is an error \n");
logging.critical("Hello this an critical error \n");