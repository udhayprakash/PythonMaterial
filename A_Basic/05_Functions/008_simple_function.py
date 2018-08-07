#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with default arguments
"""

# Function Definition
def hello(name, age=20000):
    print "%s's age is %d"%(name, age)


# Function Call 
hello('HARI')

hello('Python')
hello(365)

hello('India', 75)