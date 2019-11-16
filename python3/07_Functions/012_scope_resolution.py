#!/usr/bin/python
"""
Purpose: Python Scope Resolution
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
    print('what is pi', pi)


simple_function(pi)
