import logging.handlers as handlers
from datetime import datetime
import logging
import os

try:
    debug = 0
    # Log defining information.
    strdate = datetime.now().strftime('%Y_%b_%d_%I_%M')

    if not os.path.exists('./passWordResetLogs'):
        os.makedirs('passWordResetLogs')

    log_file = './passWordResetLogs/passwordResetLog_' + strdate + '.log'
    if not os.path.exists(log_file):
        open(log_file, 'w').close()

    logger = logging.getLogger()
    logger_fh = handlers.RotatingFileHandler(
        log_file, maxBytes=10485760, backupCount=10)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger_fh.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
        logger_fh.setLevel(logging.INFO)

    LogfileFormatter = logging.Formatter(
        '%(asctime)s [%(levelname)-8s] %(funcName)s %(message)s')
    logger_fh.setFormatter(LogfileFormatter)
    logger.addHandler(logger_fh)
except Exception as ex:
    print 'unable to create logs\n', ex
    exit(1)


logging.info('SomeThing')
