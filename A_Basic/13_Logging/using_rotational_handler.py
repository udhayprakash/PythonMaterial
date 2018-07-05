import logging
import time
import os
from logging.handlers import RotatingFileHandler
 
#----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
 
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=20,
                                  backupCount=5)
    logger.addHandler(handler)
 
    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    print "os.getcwd()", os.getcwd()
    log_file = os.getcwd() + os.sep + "test.log"
    create_rotating_log(log_file)