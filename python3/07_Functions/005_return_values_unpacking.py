#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and two return values
"""

# Function Definition
def hello():
    return 123, 45

# Function Call 
# hello()

print(hello())
result = hello()
print(f'result={result} {type(result)}')

# Unpacking
# val1 = 12231
# val2 = 1232
# val1, val2 = 12231, 1232
val1, val2 = hello()
print(f'val1 = {val1}  \nval2 = {val2}')


# List unpacking 
val1, val2 = [12231, 1232]
print(f'val1 = {val1}  \nval2 = {val2}')


# m1, m2 = [11, 22, 33]  #ValueError: too many values to unpack (expected 2)
# print(m1,m2)
