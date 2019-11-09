#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with one input argument and no return value

    function calls
        1. by positional arguments
        2. by keyword arguments
"""


# Function Definition
def hello(name):
    print("Hello " + str(name))


# Function call
# hello()                    # TypeError: hello() missing 1 required positional argument: 'name'

hello('Python')              # Hello Python

# hello('python', 'program') # TypeError: hello() takes 1 positional argument but 2 were given

hello(name='python')

# hello(name1='python')      # TypeError: hello() got an unexpected keyword argument 'name1'

