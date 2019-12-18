import logging

# Fixing the level of severity
logging.basicConfig(level=logging.DEBUG)

# To disable the logging
logging.Logger.disabled = True

logging.debug("This is a debug2")
logging.info("This is a info2")
logging.warning("This is a warning2")
logging.error("This is a error2")
logging.critical("This is a critical2")


def addition(n1, n2):
    logging.debug('Entered addition func')
    return n1 + n2


addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
addition(1, 2)
