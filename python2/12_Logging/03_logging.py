import logging

# basicConfig - to set the format of log test

logging.basicConfig(
    filename='03_logging.log',
    level=logging.DEBUG)

logging.debug("This is a debug1")
logging.info("This is a info1")
logging.warning("This is a warning1")
logging.error("This is a error1")
logging.critical("This is a critical1")
