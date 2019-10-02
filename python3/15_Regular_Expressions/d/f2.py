#!/usr/bin/python

import re

string = "This\n"
reg = re.compile(".....", re.DOTALL)
if reg.match(string):
    print("matched:", reg.match(string).group())
else:
    print(reg.match(string))

if reg.search(string):
    print("searched:", reg.search(string).group())
else:
    print(reg.search(string))
