#!/usr/bin/python
"""
Purpose: Logging
"""
import logging
import sys

print('This is print message')
sys.stderr.write("This is sys.stderr write message\n")
sys.stdout.write("This is sys.stdout write message\n")

logging.debug('This is debug message')
logging.info('This is info message')
# Default logging level is warning
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')


# SDLC -
#   dev --> staging/UAT ---> production


def addition(n1, n2):
    logging.debug('Entered addition func')
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
