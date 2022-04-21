#!/usr/bin/python
# first.py
import logging

# Time in log
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.info('Logging app started')
# logging.warning('An example logging message.')
# logging.warning('Another log message')


# basicConfig - to set the format of log test
logging.basicConfig(filename='04_logging.log',
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d-%b-%Y %I:%M:%S %p')
# based on the logging level placed, the logs will be placed.
# If the path is not specified, the log file will be created in the current working directory of python script.
logging.debug('Hello this is a debug message ')
logging.info('Hello this is information ')
logging.warning('Hello this is a warning ')
logging.error('Hello this is an error ')
logging.critical('Hello this an critical error \n')
