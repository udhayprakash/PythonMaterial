#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
List can be classified as single-­dimensional and multi­-dimensional.
List is representing using [].
List is a mutable object, which means elements in list can be changed.
It can store asymmetric data types

basic types -- int, long, float, string, bool, None, 
"""

numbers = [12, 334, 23, 2, -323]  # Homogenous list 
print('numbers=', numbers)
print('type(numbers)', type(numbers))

numbers = [12, 3.4, -0.00004, 434243432432, 'abc', True, 4 + 55 / 6]
# non-homogenous
print('numbers=', numbers)
print('type(numbers)', type(numbers))

# multi-dimensional lists
ml = [1, 2, 3, 4, 5, [6, 7, 8, [9, 10]]]
print('ml', ml)
print('type(ml)', type(ml))

print('len(ml)=', len(ml))

print('ml[3]', ml[3])
# print ml[6]  # Index Error

# print('ml[5]', ml[5])

# print('ml[5][1]', ml[5][1])
# print('ml[5][3]', ml[5][3])
# print('ml[5][3][0]', ml[5][3][0])

# # List is a mutable object 
# print('id(ml)', id(ml))
# ml[5][3][0] = '99999'
# print('ml[5][3][0]', ml[5][3][0])
# print(ml)
# print('id(ml)', id(ml))

# # String is a immutable object 
# name = 'Raj Sekhar'
# print(name) 
# print(name[0:3])
# # name[0:3] = 'Tej'    # editing not possible

# print('id(name)', id(name))
# name = 'Tej Sekhar'    # overwriting the object 
# print('id(name)', id(name))
# print(name)