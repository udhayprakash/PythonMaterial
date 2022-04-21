#!/usr/bin/python
"""
Purpose: multiple loggers
        - FileHandler
        - StreamHandler
"""
import logging
import sys
import os


# print(f'{__file__ =}')
# print(os.path.splitext(__file__))
# print(os.path.splitext(__file__)[0])
# print(os.path.splitext(__file__)[0] + '.log')
# print(os.path.join('logs', os.path.splitext(__file__)[0] + '.log'))

log_file = os.path.join('logs', os.path.splitext(__file__)[0] + '.log')


fmt = logging.Formatter('%(asctime)s %(levelname)8s %(name)s %(message)s')


errfile = logging.FileHandler(
    filename=log_file
)
errfile.setFormatter(fmt)
errfile.setLevel('ERROR')

stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setFormatter(fmt)

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

logger.addHandler(stdout)
logger.addHandler(errfile)

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')
