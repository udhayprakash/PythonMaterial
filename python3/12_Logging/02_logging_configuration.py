#!/usr/bin/python
"""
Purpose: Configuring Logging Level
"""
import logging


# Fixing the level of severity
logging.basicConfig(level=logging.DEBUG)


logging.debug("This is a debug2")
logging.info("This is a info2")
logging.warning("This is a warning2")
logging.error("This is a error2")
logging.critical("This is a critical2")
print()

logging.log(logging.DEBUG, "This is a debug3")
logging.log(logging.INFO, "This is a info3")
logging.log(logging.WARNING, "This is a warning3")
logging.log(logging.ERROR, "This is a error3")
logging.log(logging.CRITICAL, "This is a critical3")
print()

# -------------------
def addition(n1, n2):
    logging.debug('addition function - start')
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
