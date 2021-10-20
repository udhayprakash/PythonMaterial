#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with two arguments and no return value
"""


# Function Definition
def hello(name, age):
    print(f"{name}'s age is {age}")


# Function Call
# hello()
# TypeError: hello() missing 2 required positional arguments: 'name' and 'age'

# hello('sushmitha')
# TypeError: hello() missing 1 required positional argument: 'age'

# hello(27)
# TypeError: hello() missing 1 required positional argument: 'age'

print('\ncall By position')
hello('sushmitha', 27)
hello(27, 'sushmitha')

print('\ncall By keyword args')
hello(name='sushmitha', age=27)
hello(age=27, name='sushmitha')

# hello('sushmitha', 27, 'asd')
# TypeError: hello() takes 2 positional arguments but 3 were given

# hello(name='sushmitha', age=27, salary=213312)
# TypeError: hello() got an unexpected keyword argument 'salary'
