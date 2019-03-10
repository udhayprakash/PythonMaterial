#!/usr/bin/python

"""
Purpose : working with files and folders
"""

import os
import sys

print 'sys.platform:', sys.platform

if sys.platform == 'win32':
    print 'It is windows OS'
else:
    print 'It is either Linux or Unix'

dirToCheck = raw_input('Enter the directory path to check(dont enclose path with quotes):')

print 'dirToCheck', dirToCheck
print 'dirToCheck[0]', dirToCheck[0]

for (dirpath, dirnames, filenames) in os.walk(dirToCheck):
    print 'Current Path:', dirpath
    print 'Directories:', dirnames
    print 'Files:', filenames
    print '-' * 50
