#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
datatypes
===========
    int, long, float, string, bool, None

data Structures
===============
    list()
    tuple()
    set()
    dict()

    iter()

List is representing using [].
Lists can store any no.of different data types together.
List can be classified as single-­dimensional and multi­-dimensional.
List is a mutable object, which means elements in list can be changed.
It can store asymmetric data types

"""
# Homogenous list
numbers = [12, 334, 23, 2, -323]
print(f'{type(numbers)= } {numbers =}')

# non-homogenous
numbers = [12, 3.4, -0.00004, 434243432432, 'abc', True, 4 + 55 / 6, '4 + 55 / 6']
print(f'{type(numbers)= } {numbers =}')

# multi-dimensional lists
ml = [1, 2, 3, 4.3, 5, [6, 7, 8, (9, 10)]]
#     0  1  2   3   4  -------5---------
#                       0  1  2   --3--
#                                 0   1

print(f'{type(ml)= } {ml =}')
print('len(ml)=', len(ml))

# Indexing
print('ml[3]        ', ml[3])
print('type(ml[3])  ', type(ml[3]))
# print( ml[6]) # IndexError: list index out of range

print('ml[5]        ', ml[5])

print('ml[5][1]     ', ml[5][1])
print('ml[5][3]     ', ml[5][3])
print('ml[5][3][0]  ', ml[5][3][0])
# ml is a 3-dimensional list


# forward vs reverse indexing
# [1, 2, 3, 4.3, 5, [6,  7,  8, (9, 10)]]
#  0  1  2   3   4   --------5---------  - forward indexing
# -6 -5  -4  -3  -2  ------- -1 -------  - reverse indexing
#                   -4  -3  -2  -- -1 --
print('ml[-5]       ', ml[-5])
print('ml[-1]       ', ml[-1])
print('ml[-1][-1]   ', ml[-1][-1])

print(ml[-5] == ml[1])
assert ml[-5] == ml[1]

# Slicing - last value in boundary will not be included
print('ml[1:4]      ', ml[1:4])
print('ml[1:4:2]    ', ml[1:4:2])
