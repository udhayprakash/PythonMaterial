#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and default return value
"""

# Function Definition
def hello(name, age):
    print "%s's age is %d"%(name, age)
    return
    # default return is None type object

# Function Call 
result = hello('India', 75)
print "result =", result