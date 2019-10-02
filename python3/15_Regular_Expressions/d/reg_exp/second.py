#!/usr/bin/python
import re

reg = re.compile('^.....$', re.DOTALL)
my_friends = ['anil', 'sudhakar', 'vijay', 'shravanth', 'santu', 'viki\n']
for i in my_friends:
    if reg.match(i):
        print("we have a match:{}".format(i))
