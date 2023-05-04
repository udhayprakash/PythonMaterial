#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: Working with tuples
"""

mylist = [12, 34.8, 500000, [6, 8], (5,)]
print("type(mylist)", type(mylist))
print("len(mylist)", len(mylist))

mytuple = (12, 34.8, 500000, [6, 8], (5,))
print("\ntype(mytuple)", type(mytuple))
print("len(mytuple)", len(mytuple))
print(mytuple)

print()
another_tuple = (99.9,)
print("type(another_tuple)", type(another_tuple))
print("len(another_tuple) ", len(another_tuple))

# NOTE: For tuple with single element, place comma at the end
# to recognize it as tuple; else recognizes as individual element

print()
empty_tuple = ()  # tuple()
print("type(empty_tuple):", type(empty_tuple))
print("len(empty_tuple) :", len(empty_tuple))

print()
mytuple = 1, 2, 3
print("type(mytuple)    :", type(mytuple))
print("len(mytuple)     :", len(mytuple))
print(mytuple)
print()

mytuple = (1,)
print("type(mytuple)    :", type(mytuple))
print("len(mytuple)     :", len(mytuple))
print(mytuple)
