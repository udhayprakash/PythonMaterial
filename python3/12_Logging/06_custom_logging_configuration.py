#!/usr/bin/python
"""
Purpose: Adding Logging configuration 

    %(asctime)s  : displays the date and time of the log, in local time
    %(levelname)s: the logging level of the message
    %(message)s  : the message
"""
import logging

FORMAT = "%(asctime)-15s %(client_ip)s %(user)-8s %(message)s"
logging.basicConfig(format=FORMAT)
d = { 'client_ip' : '192.168.0.1', 'user' : 'fbloggs' }

logging.basicConfig(
    filename="04_logging.log", # filemode='w',
    format='%(asctime)s %(levelname)8s %(name)s %(message)s',
    datefmt='%d-%b-%Y %I:%M:%S %p',
    level=logging.DEBUG)


logging.warning("Protocol problem: %s", "connection reset", extra=d)

logger = logging.getLogger("tcpserver")
logger.warning("Protocol problem: %s", "connection reset", extra=d)




