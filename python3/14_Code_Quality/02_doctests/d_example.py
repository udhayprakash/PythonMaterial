#!/usr/bin/python
"""
Purpose: Calculating simple area.

"""
import doctest
import math


def area_rectangle(side1, side2):
    """
    (number, number) --> number.
    Calculate the area of a rectangle with side1 and side2
    and return the area.

    >>> area_rectangle(2, 8)
    16
    >>> area_rectangle(10.0, 15)
    150.0
    """
    return side1 * side2


def area_circle(radius):
    """
    (number) --> number.
    Returns the area of a circle with the specified radius.

    >>> area_circle(1)
    3.141592653589793
    >>> area_circle(2)
    12.566370614359172
    """
    return math.pi * radius ** 2


if __name__ == '__main__':
    doctest.testmod()

    print(f'area_rectangle(2, 8):{area_rectangle(2, 8)}')
