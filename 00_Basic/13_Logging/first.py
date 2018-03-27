#!/usr/bin/python
# first.py
import logging

# logging.debug('This is debug')
# logging.warning("This is a warning")
# logging.error("This is an error")

# basicConfig - to set the format of log test
#
# logging.basicConfig(filename='program.log',level=logging.DEBUG)
# logging.debug("This is a debug1")
# logging.warning("This is a warning1")
# logging.error("This is a error1")

# # Fixing the level of severity
# logging.basicConfig(level=logging.ERROR)
# logging.debug("This is a debug2")
# logging.warning("This is a warning2")
# logging.error("This is a error2")

# # TIme in log
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.info('Logging app started')
# logging.warning('An example logging message.')
# logging.warning('Another log message')
#

# basicConfig - to set the format of log test
logging.basicConfig(filename="first.log",
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d-%b-%Y %I:%M:%S %p')
# based on the logging level placed, the logs will be placed.
# If the path is not specified, the log file will be created in the current working directory of python script.
logging.debug("Hello this is a debug message ")
logging.info("Hello this is information ")
logging.warning("Hello this is a warning ")
logging.error("Hello this is an error ")
logging.critical("Hello this an critical error \n")

