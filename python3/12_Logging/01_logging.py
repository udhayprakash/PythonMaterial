import logging

logging.debug('This is debug')
logging.info("This is a info")
# Observe that debug log is not displayed in output
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is an critical")


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
