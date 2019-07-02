#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with one input argument and no return value
"""

# Function Definition
def hello(name):
    print("Hello " + str(name))


# Function Call 
# hello() # TypeError: hello() missing 1 required positional argument: 'name'
hello('raghu')
# hello('raghu', 12) # TypeError: hello() takes 1 positional argument but 2 were given
