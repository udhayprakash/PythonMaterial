#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: Working with Sets
    Properties of sets
        - creating using {} or set()
        - can't store duplicates
        - sets are unordered
        - can't be indexed
        - Empty sets need to be represented using set()
        - stores only immutable object - basic types, tuple, string
        - sets are mutable objects
"""
empty_list = []  # list()
print(f'{type(empty_list)} {empty_list}')

empty_tuple = ()  # tuple()
print(f'{type(empty_tuple)} {empty_tuple}')

empty_set = set()
print(f'{type(empty_set)} {empty_set}')
# NOTE: empty set should be defined with set()

empty_dict = {}  # dict()
print(f'{type(empty_dict)} {empty_dict}')


print('\nSets with single element ')
myset1 = {223}
print(f'{type(myset1)} {myset1 =}')

# Defining sets with some values
s1 = {1, 2, 3}
s2 = set([1, 2, 3])

print(f'{s1 =} - {type(s1)}')
print(f'{s2 =} - {type(s2)}')
assert s1 == s2

# sets are unordered
myset = {11, 22, 33, 44}
print('myset        :', myset)

# sets cant be indexed
# myset[2]  # TypeError: 'set' object is not subscriptable

# sets cant be sliced too
# myset[2:3] # TypeError: 'set' object is not subscriptable
