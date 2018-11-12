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
print "type(result)=", type(result)
print "result      =", result

# tuple unpacking 
result1, result2 = hello()
print "result1      =", result1
print "result2      =", result2
