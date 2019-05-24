#!/usr/bin/python
import re
import sys
reg = re.compile("exit",re.I)
status = raw_input("Do you want to continue or exit:")

if reg.match(status):
  print("Exiting the program")
  sys.exit(112312)
else:
  print("Please continue with the program")

