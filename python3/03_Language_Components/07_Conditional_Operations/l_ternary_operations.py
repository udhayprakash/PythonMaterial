#!/usr/bin/python
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

# Method 2 
print('Even' if num1 % 2 == 0 else 'Odd')

# ---------------------------------------------------
