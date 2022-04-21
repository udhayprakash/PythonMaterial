#!/usr/bin/python
import logging as lg

lg.basicConfig(
    filename="logs/08_logging.log",
    filemode="a",  # 'w',
    datefmt="%m/%d/%Y %I:%M:%S %p",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=lg.DEBUG,
)

size = int(input("please enter the disk size:"))

if size >= 100:
    lg.critical("The disk has hit 100%")
elif 80 <= size < 100:
    lg.error("The disk has hit above 80%")
elif 70 <= size < 80:
    lg.warning("The disk has hit above 70% and is in warning state")
else:
    lg.debug("The disk write are good!!!")
