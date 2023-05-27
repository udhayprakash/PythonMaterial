"""
Purpose: Logging error trace

Logger.exception() dumps a stack trace along with it.
Call this method only from an exception handler.

logging.exception(ex) is same as logging.error(ex, exc_info=True)
"""
import logging

# logging configuration
logging.basicConfig(
    filename="logs/07_logging.log",
    filemode="a",
    format="%(asctime)s %(levelname)8s %(name)s %(message)s",
    datefmt="%d-%b-%Y %H:%M:%S",
)

for i in range(10):
    if i % 2:
        i = str(i)

    try:
        logging.info("i + 1: %d" % (i + 1))
    except Exception as ex:
        # print(ex)
        # print(repr(ex))

        # logging.error(ex)
        # logging.error(repr(ex))

        # logging.error(ex, exc_info=True)
        logging.exception(ex)
