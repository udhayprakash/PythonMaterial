#!/usr/bin/python
"""
Purpose: converting script written in python 2.x to 3.x


HOw to run :
python C:\Python27\Tools\Scripts\2to3.py -w python_2to3_ex.py
    removing -w  means to show the differences
"""

try:
    name = raw_input('Name:')
except Exception, ex:
    print ex
else:
    print 'name', name


# https://python-future.org/
