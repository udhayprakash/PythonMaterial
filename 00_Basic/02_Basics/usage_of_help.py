#!/usr/bin/python
"""
Purpose: Demonstration of usage of help() 
on python objects
"""

dozen = 12  # int 
print type(dozen)
print dir(dozen)
print help(dozen)

mountain = "Himalayas"  # string 
print type(mountain)
print dir(mountain)
print help(mountain)
print help(mountain.isalpha)


# NOTE: help() uasage differs only for string objects