import logging
import os
import sys
from datetime import datetime

print '__file__', __file__
print 'os.path.basename(__file__)', os.path.basename(__file__)

fileName = os.path.splitext(os.path.basename(__file__))[0]
print 'fileName', fileName

try:
    myLogFolder = None
    if sys.platform == "linux" or sys.platform == "linux2":  # linux
        myLogFolder = "/usr/mylogs"
    elif sys.platform == "win32":  # windows
        myLogFolder = "C:/mylogs"
    else:
        pass
    debug = 0
    logger = logging.getLogger(fileName)
    logger.debug('my log folder is %s', myLogFolder)

    # formatting the log
    currentTimeInfo = datetime.now().strftime("%d-%b-%Y")  # ex: 27-Mar-2018
    print 'currentTimeInfo', currentTimeInfo

    if not os.path.exists(myLogFolder):
        os.makedirs(myLogFolder)

    if not os.path.exists(myLogFolder + os.sep + currentTimeInfo):
        os.makedirs(myLogFolder + os.sep + currentTimeInfo)
    log_file = myLogFolder + os.sep + currentTimeInfo + '/' + fileName + '.log'

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

    fileHandler = logging.FileHandler(log_file, mode='w')  # default is append mode
    logger.addHandler(fileHandler)

except:
    print "Exception occurred.Unable to perform logging."
    sys.exit(1)

logger.debug("Hello this is a debug message \n")
logger.info("Hello this is information \n")
logger.warning("Hello this is a warning \n")
logger.error("Hello this is an error \n")
logger.critical("Hello this an critical error \n")
