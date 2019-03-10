#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with one input argument and no return value
"""

# Function Definition
def hello(name):
    print "Hello " + str(name)


# Function Call 
# hello() # TypeError: hello() takes exactly 1 argument (0 given)
hello('Python')
# hello('Python', 'programming')# TypeError: hello() takes exactly 1 argument (2 given)

hello(5)