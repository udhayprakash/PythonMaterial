#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 

Immutable Objects - int,  float, str, tuple, fronzenset
Mutable Objects   - list, set, dictionary 
"""
pi = 3.141617  # immutable  - call by value
details = {  # mutable  - call by reference
    'lang': 'Python'
}


def simple_function(phi, details1):
    print("Inside function call, pi", phi, "details", details1)
    phi = 78
    details1['framework'] = 'django'
    print("Before function exit, pi", phi , "details", details1)



print("before function call, pi", pi, "details", details)
simple_function(pi, details)
print("after function call, pi", pi, "details", details)

# print 'phi=', phi # NameError: name 'phi' is not defined
