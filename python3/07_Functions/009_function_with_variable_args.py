#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with variable arguments
    variadic functions
"""
# built-in
# print is the simplest example of variadic function
print(12)
print(12, '34', 'three')

# Function Definition
def hello(*feed_in):
    print("\ntype(feed_in)",  type(feed_in))
    print("inputs are "+ str(feed_in))


# Function Call 
hello()            # 0 inputs
hello('HARI')      # 1 input

hello('Python')
hello(365)

hello('India', 75)

hello('India', 75, 34, 'sdas', 342432, 212.34)