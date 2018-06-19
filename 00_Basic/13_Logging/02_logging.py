import logging

# basicConfig - to set the format of log test

logging.basicConfig(filename='program.log',
                    level=logging.DEBUG)
logging.debug("This is a debug1")
logging.warning("This is a warning1")
logging.error("This is a error1")
