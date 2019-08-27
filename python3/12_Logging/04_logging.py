#!/usr/bin/python
# first.py
import logging

# Time in log
logging.basicConfig(
    filename="04_logging.log",
    # format='%(asctime)s %(levelname)8s %(name)s %(message)s',
    format='%(asctime)s - %(levelname)8s - %(name)s - %(message)s',
    datefmt='%d-%b-%Y %I:%M:%S %p',
    level=logging.DEBUG)
logging.info('Logging app started')
logging.warning('An example logging message.')
logging.warning('Another log message')


# # based on the logging level placed, the logs will be placed.
# # If the path is not specified, the log file will be created in the current working directory of python script.
def addition(n1, n2):
    logging.debug('Entered addition func')
    return n1 + n2

addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
