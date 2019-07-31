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
result1, result2 = hello() #123, 45 
print("result1      =", result1)
print("result2      =", result2)

#####################
def hello1():
    return [11, 22, 33]


# list unpacking 
res1, res2, res3 = hello1()
print("res1      =", res1)
print("res2      =", res2)
print("res3      =", res3)

# m1, m2 = [11, 22, 33]  #ValueError: too many values to unpack (expected 2)
# print(m1,m2)
