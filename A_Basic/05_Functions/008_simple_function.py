#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with default arguments
"""

# Function Definition
def hello(name='BINDU', age=200):
    print "%s's age is %d"%(name, age)

# NOTE: default arguments should be at the end

# Function Call 
hello('HARI')

hello('Python')
hello(365)

hello('India', 75)

hello()