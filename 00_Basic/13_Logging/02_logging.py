import logging

# logging.basicConfig(filename='program.log',level=logging.DEBUG)


# Fixing the level of severity
logging.basicConfig(
    level=logging.ERROR)

logging.debug("This is a debug2")
logging.warning("This is a warning2")
logging.error("This is a error2")
logging.critical("This is a critical2")
