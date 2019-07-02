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
# hello() # TypeError: hello() takes exactly 1 argument (0 given)

# hello('Python')  # TypeError: hello() missing 1 required positional argument: 'age'

hello('India', 75)
hello(75, 'India')

hello(name='India', age=75)
hello( age=75, name='India')
