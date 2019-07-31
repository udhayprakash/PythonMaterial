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
# hello()
# hello('Python')
hello('Python', 28) 
hello(['Python'], 28) 
# hello('Python', 28, 12) 

hello(28, 'Python') 


hello(name='Python', age=28)
hello( age=28, name='Python')