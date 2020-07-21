#!/usr/bin/python
"""
Purpose: converting script written in python 2.x to 3.x


HOw to run :
python -m lib2to3 -w python_2to3_ex.py
    removing -w  means to show the differences
"""

try:
    name = raw_input('Name:')
except Exception, ex:
    print ex
else:
    print 'name', name 