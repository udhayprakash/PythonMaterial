#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
List can be classified as single­dimensional and multi­dimensional.
List is representing using [].
List is a mutable object, which means elements in list can be changed.
It can store asymmetric data types
"""


numbers = [12, 334, 23, 2, -323]   # Homogenous list 
print 'numbers=', numbers
print 'type(numbers)', type(numbers)


alphabets = ['a', 'b', 'c']


print numbers + alphabets
print numbers.__add__(alphabets)


ml= [1, 2, 3, 4, 5, [6, 7, 8, [9, 10]]]

print ml[3]
# print ml[6]

print len(ml)
print ml[5]

print ml[5][1]
print ml[5][3]
print ml[5][3][0]