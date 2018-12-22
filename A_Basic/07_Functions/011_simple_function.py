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
    print "Inside function call, pi", pi, "details", details
    # pi = 78 # UnboundLocalError
    details['framework'] = 'django'
    print "Simple Function"


print "before function call, pi", pi, "details", details
simple_function()
print "after function call, pi", pi, "details", details

