#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with one input argument and no return value
"""

# Function Definition
def hello(name):
    print("Hello " + str(name))

# hello() # TypeError: hello() missing 1 required positional argument: 'name'
hello('Python')

# hello('Python', "programming")
# TypeError: hello() takes 1 positional argument but 2 were given

hello(name='Python')
# hello(name1='Python')
# TypeError: hello() got an unexpected keyword argument 'name1'
