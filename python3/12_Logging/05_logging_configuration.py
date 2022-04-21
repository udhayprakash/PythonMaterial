#!/usr/bin/python
"""
Purpose: Adding Logging configuration

--------------------------------------------------------------------------------------------------------------
Format              Description
--------------------------------------------------------------------------------------------------------------
%(name)s	        Name of the logger (logging channel).
%(levelno)s	        Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
%(levelname)s	    Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
%(pathname)s	    Full pathname of the source file where the logging call was issued (if available).
%(filename)s	    Filename portion of pathname.
%(module)s	        Module (name portion of filename).
%(funcName)s	    Name of function containing the logging call.
%(lineno)d	        Source line number where the logging call was issued (if available).
%(created)f	        Time when the LogRecord was created (as returned by time.time()).
%(relativeCreated)d	Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
%(asctime)s	        Human-readable time when the LogRecord was created. By default this is of the form “2003-07-08 16:49:45,896” (the numbers after the comma are millisecond portion of the time).
%(msecs)d	        Millisecond portion of the time when the LogRecord was created.
%(thread)d	        Thread ID (if available).
%(threadName)s	    Thread name (if available).
%(process)d	        Process ID (if available).
%(processName)s	    Process name (if available).
%(message)s	        The logged message, computed as msg % args.
"""
import logging

# Time in log
logging.basicConfig(
    filename="logs/05_logging.log",  # filemode='w',
    format="%(asctime)s %(levelname)8s %(name)s %(message)s",
    datefmt="%d-%b-%Y %I:%M:%S %p",
    level=logging.DEBUG,
)

logging.info("Logging app started")
logging.warning("An example logging message.")
logging.warning("Another log message")
print()

# NOTE: based on the logging level placed, the logs will be placed.
# If the path is not specified, the log file will be created in
# the current working directory of python script.


def addition(n1, n2):
    logging.debug("Entered addition func")
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
