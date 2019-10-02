#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and no return value
"""


# Function Definition
def hello(name, age):
    # print("%s's age is %d"%(name, age))
    print("{}'s age is {}".format(name, age))


# Function Call 
# hello() # TypeError: hello() missing 2 required positional arguments: 'name' and 'age'

# hello('Gudo')
hello('Gudo', 77)
hello(77, 'Gudo')

hello(name='Gudo', age=77)
hello(age=77, name='Gudo')
