#!/usr/bin/python
# third.py
import logging

'''
	Purpose: To display the logs in console only
'''

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)8s - %(name)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# # creating you logger.
logger = logging.getLogger('myapp')  # 'logger' object was created
logger.setLevel(logging.DEBUG)
#
# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
