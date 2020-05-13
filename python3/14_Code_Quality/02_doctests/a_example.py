#!/usr/bin/python
"""
Purpose: Adding doctest
"""
import doctest


def square(x):
    """
    This function will return the square value of given value.
    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(-0.002)
    4e-06
    >>> square(0.002)
    4e-06
    """
    return x * x 

if __name__ == '__main__':
    doctest.testmod()
    print(square(2)) 