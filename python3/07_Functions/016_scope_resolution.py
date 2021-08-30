#!/usr/bin/python3
"""
Purpose: Python Scope Resolution

    Python scope resolution is based on the LEGB rule,
        which is shorthand for Local, Enclosing, Global, Built-in.
        LEGB
            L - Local
            E - Enclosed
            G - Global
            B - Built-in

            E -> L -> G -> B
"""
from pprint import pprint

from math import pi
print('built-in scope    ', pi)          # Built-in scope

pi = 3.14                               # Global Scope
print('Global Scope      ', pi)  


def simple_function(pi):
    pi = 333                            # Local scope
    print('Local Scope       ', pi)
    values = [pi for pi in (1, 2, 34)]  # Enclosed scope
    print('what is pi doing? ', pi, values)
    pprint(locals())

simple_function(pi)

pprint(globals())