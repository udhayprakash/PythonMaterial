#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and two return values
"""

# Function Definition
def hello():
    return 123, 45

# Function Call 
result = hello()
print("type(result)=", type(result))
print("result      =", result)

# tuple unpacking 
result1, result2 = hello()
print("result1      =", result1)
print("result2      =", result2)

# list unpacking 
r1, r2, r3 = [11, 22, 33]
print(r1,r2, r3)

# m1, m2 = [11, 22, 33]  #ValueError: too many values to unpack (expected 2)
# print(m1,m2)

