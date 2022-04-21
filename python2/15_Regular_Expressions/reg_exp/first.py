#!/usr/bin/python
# to find out if answer is yes or no.
import re
reg = re.compile('yes',re.I)

answer = raw_input('please enter the answer:')
if reg.match(answer):
  print 'you are welcome'
else:
  print 'you will be welcome next time'
