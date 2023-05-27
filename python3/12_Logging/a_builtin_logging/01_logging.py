"""
Purpose: Logging
"""
import logging
import sys

# print(dir(logging))


print("This is print message")
sys.stderr.write("This is sys.stderr write message\n")
sys.stdout.write("This is sys.stdout write message\n")
print()

logging.debug("This is debug message")
logging.info("This is info message")

# Default logging level is warning
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
print()

# Formatting logs
logging.error("This is %dth error of %s application" % (5, "polls"))
logging.error("This is %dth error of %s application", 5, "polls")

print("This is %dth error of %s application", 5, "polls")
print("This is 5th error of polls application", 5, "polls")

# logging.error('This is 5th error of polls application', 5, 'polls')
# TypeError: not all arguments converted during string formatting
print()

# F-strinsg replace is next things
logging.error("This is {}th error of {} application".format(5, "polls"))
logging.error(f"This is {5}th error of {'polls'} application")

# SDLC -
#   dev --> testing --> staging/UAT ---> production


def addition(n1, n2):
    logging.debug("addition function - start")
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
