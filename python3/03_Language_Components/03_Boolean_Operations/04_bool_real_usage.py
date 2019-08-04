#!/usr/bin/python
"""
Purpose: Boolean Operations
"""

num1 = -0.000000056

print('bool(num1 != 0)', bool(num1 != 0))

if num1 < 7 and num1 < 8:
    print('num1 < 7 and num1 < 8')

if not (num1 > 7 and num1 < 8):
    print('not (num1 > 7 and num1 < 8)')

if num1:  # num1 != 0 
    print("a=", num1)


if not 0:
    print("hello")

while 1:
    print("hello")
    break 


bool( num1>=9)
bool(False)
False

if not num1>=9:
    print("a=", num1)


# Question 
bool('False')