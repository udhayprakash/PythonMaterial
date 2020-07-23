#!/usr/bin/python

import re
course = raw_input("please enter the course name:")
reg = re.compile('python',re.I)
if reg.search(course):
  print "you have selected the %s course" %(reg.search(course).group())
else:
  print "you have not selected the %s course" %(course)
