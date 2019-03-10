import os
import sys
import logging
from datetime import datetime

print __file__
print os.path.basename(__file__)


fileName = os.path.basename(__file__).split('.')[0]
print fileName

try:
    myLogFolder = None
    if sys.platform == "linux" or sys.platform == "linux2": # linux
        myLogFolder = "/usr/mylogs"
    elif sys.platform == "win32":                       # windows
        myLogFolder = "C:/mylogs"
    else:
        pass 
    debug = 0
    logging.debug('my log folder is %s', myLogFolder)
    # formatting the log
    currentTimeInfo = datetime.now().strftime("%d-%b-%Y")   # ex: 20-Jul-2016
    print currentTimeInfo
    if not os.path.exists(myLogFolder):
        os.makedirs(myLogFolder)
    if not os.path.exists(myLogFolder + '/' + currentTimeInfo):
        os.makedirs(myLogFolder + '/' + currentTimeInfo)
    log_file = myLogFolder + '/' + currentTimeInfo + '/' + fileName +'.log'
    
    if not os.path.exists(log_file):
        open(log_file, 'w').close()
    logger = logging.getLogger()

    myLogHandler = logging.StreamHandler(sys.stdout)
    if debug:
        logger.setLevel(logging.DEBUG)
        myLogHandler.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
        myLogHandler.setLevel(logging.INFO)

    LogfileFormatter = logging.Formatter(
        '%(asctime)s [%(process)-5d] [%(funcName)-10s] [%(levelname)-8s] %(message)s')
    
    myLogHandler.setFormatter(LogfileFormatter)
    logger.addHandler(myLogHandler)

    fileHandler = logging.FileHandler(log_file, mode='w')
    logger.addHandler(fileHandler)

except:
    print "Exception occurred.Unable to perform logging."
    sys.exit(1)


logging.debug("Hello this is a debug message \n")
logging.info("Hello this is information \n")
logging.warning("Hello this is a warning \n")
logging.error("Hello this is an error \n")
logging.critical("Hello this an critical error \n")