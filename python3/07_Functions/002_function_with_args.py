#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with one input argument and no return value
"""

# Function Definition
def hello(name):
    print("Hello " + str(name))


# Function Call 
# hello() # TypeError: hello() missing 1 required positional argument: 'name'#
hello('python')
hello(123)

# hello('python', 123) TypeError: hello() takes 1 positional argument but 2 were given

hello(name=123)
# hello(name1=123) # TypeError: hello() got an unexpected keyword argument 'name1'
