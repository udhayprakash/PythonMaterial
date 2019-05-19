#!/usr/bin/python
"""
Purpose: Boolean Operations
"""

print('bool(9>34)', bool(9>34))  # bool(False) => False

if not 0:
    print("hello")

while 1:
    print("hello")
    break 

num1 = -0.000000056
if num1:
    print("a=", num1)


if num1 >= 9:
    print("a=", num1)


# bool( num1>=9)
# bool(False)
# False

if not num1>=9:
    print("a=", num1)


# Question 
bool('False')