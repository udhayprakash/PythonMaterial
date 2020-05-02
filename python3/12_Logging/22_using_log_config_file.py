#!/usr/bin/python
"""
Purpose: Using logging configuration file 
"""

import logging
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), '18_logging.conf')
logging.config.fileConfig(log_file_path)


# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
