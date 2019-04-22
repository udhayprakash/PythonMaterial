#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and no return value
"""

# Function Definition
def hello(name, age):
    # print "%s's age is %d"%(name, age)
    print("{}'s age is {}".format(name, age))


# Function Call 
# hello() # TypeError: hello() takes exactly 1 argument (0 given)

# hello('Python')  # TypeError: hello() takes exactly 2 arguments (1 given)

hello('India', 75)
hello(name='India', age=75)
hello( age=75, name='India')
