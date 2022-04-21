#!/usr/bin/python

import re

f = open('file1.txt')
reg = re.compile('.*@.*')
for line in f:
  if reg.search(line):
    print reg.search(line).group()

'''
f = open("file1.txt")
for line in f:
  print line
'''
