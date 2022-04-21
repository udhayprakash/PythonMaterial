#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with variable keyword arguments

NOTE: PEP8 recommends not use more than 7 args for an function
"""
# Function Definition


def hello(*given, **feed_in):
    print("\ntype(given)  ", type(given))
    print("type(feed_in) ", type(feed_in))

    print("given   " + str(given))
    print("feed_in " + str(feed_in))
    print("-" * 20)


# Function Call
hello()  # 0 inputs

hello("santosh")  # 1 input
hello(name="santosh")  # 1 input

hello("siddanth", 34)  # 2 args
hello(name1="siddanth", age=34)  # 2 args

hello(212.34, "India", 75, number=34, mystring="sdas", largest=342432)
