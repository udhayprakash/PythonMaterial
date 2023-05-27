"""
Purpose: Adding Logging configuration

    %(asctime)s  : displays the date and time of the log, in local time
    %(levelname)s: the logging level of the message
    %(message)s  : the message
"""
import logging

logging.basicConfig(
    format="%(asctime)-15s %(client_ip)s %(name)9s %(user)-8s %(message)s"
)

d = {"client_ip": "192.168.0.1", "user": "fbloggs"}

logging.info("This is info message", extra=d)
logging.error("This is error message", extra=d)


# Method 1
logging.basicConfig(
    filename="logs/06_logging.log",  # filemode='w',
    format="%(asctime)s %(levelname)8s %(name)s %(message)s",
    datefmt="%d-%b-%Y %I:%M:%S %p",
    level=logging.DEBUG,
)
logging.warning("Protocol problem: %s", "connection reset", extra=d)


# Method 2
logger = logging.getLogger("TCPserver")
logger.warning("Protocol problem: %s", "connection reset", extra=d)

logger2 = logging.getLogger("UDPserver")
logger2.warning("Protocol problem: %s", "connection reset", extra=d)

logger3 = logging.getLogger("myApp")
logger3.warning("Protocol problem: %s", "connection reset", extra=d)
