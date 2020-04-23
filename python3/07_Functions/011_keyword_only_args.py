#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with Keyword ONLY args

    Named arguments appearing after '*' can only be 
    passed by keyword

    Present only in Python 3.X
"""


# Function Definition
def recv(maxsize,  block=True):
    print("\ntype(maxsize)  ", type(maxsize))
    print("type(block) ", type(block))

    print("maxsize   " + str(maxsize))
    print("block     " + str(block))
    print('-' * 20)


# Function Call 
recv(1234)
recv(maxsize=1234, block=False)
recv(1234, block=False)


# recv(1234, False) # TypeError: recv() takes 1 positional argument but 2 were given

"""
 Recommended order for the arguments
    def func(positional, keyword=value, *args, **kwargs):
        pass
"""