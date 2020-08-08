#!/usr/bin/python3
"""
Purpose: Function with variable arguments
    
    variadic functions - functions which can process any no. of arguments
"""
# built-in
# print is the simplest example of variadic function
print(12, '34', 'three', 'India', None, True, 'sdas', 342432, 212.34)
print(12, '34', 'three')
print(12, '34')
print(12)
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
addition(10, 20, 30, True, 30, '20', None, 30)

#-----------------------------------
print()
def print_function(*args):
    for each_arg in args:
        print(each_arg, sep=' ', end=' ')
    print()

print_function()
print_function(12)
print_function(12, '34')
print_function(12, '34', 'three')
print_function(12, '34', 'three', 'India', 75, 34, 'sdas', 342432, 212.34)
