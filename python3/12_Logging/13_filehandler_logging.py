#!/usr/bin/python
"""
Purpose: Demonstartion of logging
"""
import logging

# defining the handler
han = logging.FileHandler('logs/14_logging.log')

# Formatter
formate = logging.Formatter('%(asctime)s - %(levelname)8s - %(name)s - %(message)s')

# creating the formatter for our handle
han.setFormatter(formate)

# set my logger
logger = logging.getLogger('newApp')

# Adding the handler to the logger.
logger.addHandler(han)


logger.debug('Hello this is a debug message')
logger.info('Hello this is information')
logger.warning('Hello this is a warning\n')
logger.error('Hello this is an error\n')
logger.critical('Hello this an critical error\n')

logging.debug('Hello this is a debug message1')
logging.info('Hello this is information 1\n')
logging.warning('Hello this is a warning 1\n')
logging.error('Hello this is an error 1\n')
logging.critical('Hello this an critical error 1\n')

# It is different from logging.critical("Hello this an critical error")
