#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 
"""
pi = 3.141617  # immutable
details = {  # mutable
    'language': 'Python',
    'version': '2.7.14'
}


def simple_function():
    """
    mutable object can be edited within function without passing as args
    immutable object CANT be edited within function without passing as args
    """
    print "Inside function call, pi", pi, "details", details
    # pi = 78 # UnboundLocalError: local variable 'pi' referenced before assignment
    details['version'] = '3.8.1'


print "before function call, pi", pi, "details", details
simple_function()
print "after function call, pi", pi, "details", details

