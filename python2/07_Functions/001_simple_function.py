#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with no arguments and no return value
"""

# Function Definition
def hello():
    print "Hello world"
    #return None - default


print hello
print 'callable(hello)', callable(hello)
fruit = 'apple'
print 'callable(fruit)', callable(fruit)


# Function Call 
hello()
print hello()
