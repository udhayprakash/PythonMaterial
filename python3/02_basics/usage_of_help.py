#!/usr/bin/python
"""
Purpose: Demonstration of usage of help() 
on python objects
"""

dozen = 12  # int 
print(type(dozen))
print(dir(dozen))
help(dozen)

print('='*40)
mountain = "Himalayas"  # string
print(type(mountain))
print(dir(mountain))
# help(mountain)
help(str)
help(mountain.isalpha)


# NOTE: help() usage differs only for string objects
