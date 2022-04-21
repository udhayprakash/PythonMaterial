#!/usr/bin/python

import os

# popen() is similar to open()
file = open('testfile.txt', 'w')
file.write('Hello')
file.close()
file = open('testfile.txt', 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen('testfile.txt', 'w')
file.write('Hello')
# File not closed, shown in next function.
os.close(file)
