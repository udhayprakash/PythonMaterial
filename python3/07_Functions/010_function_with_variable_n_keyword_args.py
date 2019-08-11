#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with variable keyword arguments
"""

# Function Definition
def hello(*given, **feed_in): # 
    print("\ntype(given)  ",  type(given))
    print("type(feed_in) ",  type(feed_in))

    print("given   "+ str(given))
    print("feed_in "+ str(feed_in))
    print('-'*20)

# Function Call 
hello()                         # 0 inputs

hello('HARI')                   # 1 input

hello('HARI', 'chaitra')        # 2 inputs
hello('India', 75, 34, 'sdas', 342432, 212.34)

hello(std1='HARI')              # 1 input
hello(std1='HARI', std2='chaitra')# 2 inputs

hello(language='Python')
hello(years=365)

hello(country='India', age=75)

hello(212.34, 'India', 75, 
        number=34, 
        mystring='sdas', 
        larger_number=342432)