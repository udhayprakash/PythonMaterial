#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and no return value
"""


# Function Definition
def hello(name, age):
    print(f"{name}'s age is {age}")


# Function call
# hello()                       # TypeError: hello() missing 2 required positional arguments: 'name' and 'age'

# hello('Gudo van')             # TypeError: hello() missing 1 required positional argument: 'age'
# hello('GUdo Van', 63, 'sad')  # TypeError: hello() takes 2 positional arguments but 3 were given

hello('GUdo Van', 63)
hello(63, 'GUdo Van')

# keyword args based call
hello(name='GUdo Van', age=63)
hello(age=63, name='GUdo Van')
