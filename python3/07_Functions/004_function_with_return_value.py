#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and default return value
"""

# Function Definition
def hello(name, age):
    print("%s's age is %d"%(name, age))
    # default return is None type object
    # return None
    # return 12
    # return 12.0
    # return 12.0,
    # return 12,,    # SyntaxError
    # return (12,),
    # return {12:34}
    return "%s's age is %d"%(name, age)

# Function Call 
# print(hello('India', 75))

result = hello('India', 75)
print("result =", result, type(result))