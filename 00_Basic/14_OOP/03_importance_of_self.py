#!/usr/bin/python
"""
Purpose: OOP demos
"""
__author__ = 'Developer Name'

class Name:
    def __init__(self):   # constructor
        print('I am a constructor. ')
        print('I will be called, the moment you create an instance')

    def displayNames(self):
        print('Existing names: ramesh, suresh, mahesh, ganesh')

n = Name()


# we need to call all other methods, except constructor
n.displayNames()

