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
from math import pi
print('built-in scope   ', pi)          # Built-in scope

pi = 3.14                               # Global Scope
print('Global Scope     ', pi)  


def simple_function(pi):
    pi = 333                            # Local scope
    print('Local Scope       ', pi)
    values = [pi for pi in (1, 2, 34)]  # Enclosed scope
    print('what is pi doing? ', pi, values)


simple_function(pi)
print()
# ------------------------------------
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        # global x
        x = 2
        print("inner :", x)

    inner()
    print("outer :", x) 
                # not effected when global
                # effected when nonlocal

outer()
print("global:", x) 
        # effected when global
        # not effected when nonlocal


# NOTE: 
# 1. If a variable is initialized with global, 
#    changes to it with be reflected globally(through out the script)
# 2. If a variable is initialized with "nonlocal", 
#    changes to it will be reflected one-level above it 
