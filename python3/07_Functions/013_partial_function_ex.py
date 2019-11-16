#!/usr/bin/python
"""
Purpose: Partial functions
"""
import functools


# ordinary function
def multiply(x, y):
    return x * y


print(multiply(2, 4))
print(multiply(2, 14))
print(multiply(2, 2))

# -------------------------------------------
multiply_2 = functools.partial(multiply, 2)

print(f'multiply_2      :{multiply_2}')
print(f'type(multiply_2):{type(multiply_2)}')

assert multiply_2(4) == multiply(2, 4)
assert multiply_2(14) == multiply(2, 14)

'''
Assignments
------------
1) Develop a calculator software which does +, -, *, / operations
    Then, make use of partial functions to optimize your solution.
'''