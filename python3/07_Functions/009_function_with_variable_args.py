#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with variable arguments
    variadic functions
"""
# built-in
# print is the simplest example of variadic function
print()
print(12)
print(12, '34', 'three')
print(12, '34', 'three', 'India', 75, 34, 'sdas', 342432, 212.34)
print()


# Function definition
def addition(*nums):
    print(f'\nnums        :{nums}')
    print(f'type(nums)  :{type(nums)}')


# Function call
addition()
addition(10)
addition(10, 20)
addition(10, 20, 30)
addition(10, 20, 30, 20, 30, 20, 30, 20, 30)
