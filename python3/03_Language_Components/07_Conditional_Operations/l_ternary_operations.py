#!/usr/bin/python3
"""
Purpose: Ternary operation usage 

Useful, when there is  one condition and two ways
"""
num1 = 10

# Method 1
if num1 % 2 == 0:
    print('Even')
else:
    print('Odd')

# Method 2 - using ternary operation
print('Even' if num1 % 2 == 0 else 'Odd')

# ------
if num1 % 2:
    print('Odd')
else:
    print('Even')

print('Odd' if num1 % 2 else 'Even')

print('non-zero' if num1 != 0 else 'zero')
print('non-zero' if num1 else 'zero')
print('non-zero' if not num1 == 0 else 'zero')


# Javascript: conditon: success_case, failure_case
# Python    : success_case if condition else failure_case
