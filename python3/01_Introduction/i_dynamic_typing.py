#!/usr/bin/python
"""
Purpose: Python is a dynamic Typed Language

progr. language 
    1. static typed language
        - first declare the variables, & then use them
            int a, float b
            a = 10
    2. Dynamic typed language
        - create when you need. No declaration needed
            num1 = 123
""" 
num1 = 123
print('num1')
print(num1)

print('num1 =', num1, type(num1))

num1 = 123.234
print('num1 =', num1, type(num1))

num1 = '123.234'
print('num1 =', num1, type(num1))

num1 = None
print('num1 =', num1, type(num1))

num1 = True
print('num1 =', num1, type(num1))

num1 = 3 + 4j
print('num1 =', num1, type(num1))