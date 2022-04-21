#!/usr/bin/python
import re

string = 'Today is sunday'
reg = re.compile(string)
print type(reg)
match = raw_input('please try match string:')
print reg.match(match).group()
