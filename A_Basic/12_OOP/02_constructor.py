#!/usr/bin/python
"""
Purpose: OOP demos
"""
__author__ = 'Developer Name'

# __new__
class Name:
    def __init__(self):  # constructor
        print('I am a constructor. ')
        print('I will be called, the moment you create an instance')


n = Name()
m = Name()
p = Name  # class object assignment

p()


print
print '----------calling contructor'
n.__init__()