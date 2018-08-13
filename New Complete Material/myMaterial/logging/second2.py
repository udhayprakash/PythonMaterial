#!/usr/bin/python
# second2.py
import logging as lg


lg.basicConfig(filename="disk.log",filemode='a',datefmt='%m/%d/%Y %I:%M:%S %p',format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',level=lg.INFO)

size = int(raw_input("please enter the disk size:"))

if size >= 100:
  lg.critical("The disk has hit 100%")
elif size > 80 and size < 100:
  lg.error("The disk has hit above 80%")
elif size > 70 and size < 80:
  lg.warning("The disk has hit above 70% and is in warning state")
else:
  lg.info("The disk write are good!!!")
