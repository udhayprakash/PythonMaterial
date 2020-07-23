#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with default arguments
"""

# Function Definition
def hello(height,name='BINDU', age=200):
    # print "%s's age is %d with height %d"%(name, age, height)
    print "{0}'s age is {1} with height {2}".format(name, age, height)

# NOTE: default arguments should be at the end

# Function Call 
hello(1)  # mandatory args shoud be given

hello('HARI')
hello(1, 'HARI')

hello('Python')
hello(1,365)

hello(1,'India', 75)
