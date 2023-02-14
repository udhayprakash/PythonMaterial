#!/usr/bin/python
"""
Purpose: logging to log file
    .log
"""
import logging

# basicConfig - to set the format of log test

logging.basicConfig(
    filename="logs/04_logging.log", filemode="w", level=logging.DEBUG  # 'a' - default
)

logging.debug("This is a debug1")
logging.info("This is a info1")
logging.warning("This is a warning1")
logging.error("This is a error1")
logging.critical("This is a critical1")


# --------------------------------------------
def addition(n1, n2):
    logging.debug("Entered addition func")
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
