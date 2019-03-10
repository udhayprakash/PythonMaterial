import logging

logging.debug('This is debug')
logging.info("This is a info")
# Observe that debug log is not displayed in output
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is an critical")


# dev --> staging/UAT ---> production


def hello(name):
    logging.debug('entered teh function')

    