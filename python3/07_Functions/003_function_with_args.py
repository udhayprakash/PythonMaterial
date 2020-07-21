#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with one input argument and no return value

    function calls
        1. by positional arguments
        2. by keyword arguments
"""

def hello_word():
    print('Hello function is called')

hello_word()

# Function Definition
def hello(name):
    print("Hello " + name)


# Function Call 
# hello()                     
# TypeError: hello() missing 1 required positional argument: 'name'

hello('Python')    #---> call by positional arguments

# hello('Python', 'program')  
# # TypeError: hello() takes 1 positional argument but 2 were given

hello(name='python')   #-----> call by keyword arguments
# hello(name1='python')   
# # TypeError: hello() got an unexpected keyword argument 'name1'
