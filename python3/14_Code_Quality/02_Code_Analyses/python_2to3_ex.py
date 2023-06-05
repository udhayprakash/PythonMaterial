#!/usr/bin/python
"""
Purpose: converting script written in python 2.x to 3.x


How to run :
    python -m lib2to3 -w python_2to3_ex.py
    removing -w  means to show the differences
"""
nums = range(10)

try:
    name = input("Name:")
except Exception as ex:
    print(ex)
else:
    print("name", name)
