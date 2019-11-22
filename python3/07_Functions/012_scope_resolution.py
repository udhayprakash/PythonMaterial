#!/usr/bin/python
"""
Purpose: Python Scope Resolution
Python scope resolution is based on the LEGB rule,
	which is shorthand for Local, Enclosing, Global, Built-in.
    LEGB
        L -local
        E - Enclosed
        G - Global
        B - Built-in
"""

from math import pi

print('built-in scope', pi)  # Built-in scope

pi = 3.14
print('Global Scope', pi)  # Global Scope


def simple_function(pi):
    pi = 3333
    print('Local Scope', pi)
    values = [pi for pi in (1, 2, 34)]  # Enclosed scope
    print('what is pi doing? ', pi, values)


simple_function(pi)
