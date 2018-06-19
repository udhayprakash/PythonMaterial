#!/usr/bin/python
import logging

# create logger
logger = logging.getLogger('my app')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

value = int(raw_input("Please enter the disk space"))
if value == 100:
    logger.critical("we are in a critical state")
elif value < 90 and value > 80:
    logger.warning("This is warning information")
elif value < 80 and value > 70:
    logger.error("This is error information")
else:
    logger.debug("All is fine")

# L.info("This is a infomation")
# L.debug("This is debug information")
# L.error("This is error information")
# L.warning("This is warning information")
# L.critical("This is critical information")
