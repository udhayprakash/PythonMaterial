#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and default return value
"""

# Function Definition
def hello(name, age):
    print("%s's age is %d"%(name, age))
    # return 
    # return None
    # return 3212321
    # return 3212321.23321
    # return 3212321.23321,
    # return 3212321.23321,123
    # return 2,,  #SyntaxError: invalid syntax
    # return (2,),
    # return 'asdas'
    return 12 + 1231/3%23 - 234
    
# NOTE: return will be last executing statement in functions

# Function Call 
# print(hello('India', 75))

result = hello('India', 75)
print(f'result = {result} {type(result)}')