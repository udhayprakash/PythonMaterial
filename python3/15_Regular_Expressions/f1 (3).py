#!/usr/bin/python
import re

string = input("please enter the name of the string:")
reg = re.compile('^.....$',re.DOTALL)
if reg.match(string):
  print("our string is 5 character long - %s" %(reg.match(string).group())
else:
  print("our string is not 5 characate long")
