#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 
"""
pi = 3.141617  # immutable  - call by value
details = {  # mutable  - call by reference
    'language': 'Python',
    'version': '2.7.14'
}


def simple_function(phi):
    print "Inside function call, pi", phi, "details", details
    phi = 78
    details['framework'] = 'django'
    print "Before function exit, pi", phi, "details", details



print "before function call, pi", pi, "details", details
simple_function(pi)
print "after function call, pi", pi, "details", details


