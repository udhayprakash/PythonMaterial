import logging
import time

from logging.handlers import TimedRotatingFileHandler


# ----------------------------------------------------------------------
def create_timed_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)8s - %(name)s - %(message)s')

    handler = TimedRotatingFileHandler(path,
                                       when="M",  # Minutes
                                       interval=1,
                                       backupCount=5)

    # S - Seconds 
    # M - Minutes 
    # H - Hours 
    # D - Days 
    # W0-w6 - weekday(0-Monday)
    # midnight

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    for _ in range(100000000):
        logger.info("This is a test!")
        time.sleep(10)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "timed_test.log"
    create_timed_rotating_log(log_file)
