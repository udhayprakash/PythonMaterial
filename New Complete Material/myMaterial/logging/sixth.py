#!/usr/bin/python
# fifth.py
import logging
import os



# create logger

#logger = logging.getLogger(__name__)										# method 1
#logger = logging.getLogger(__file__)										# method 2
#logger = logging.getLogger(os.path.basename(__file__)) 					# method 3
logger = logging.getLogger('myApp')										    # method 4
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
