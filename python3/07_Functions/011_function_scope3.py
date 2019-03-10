#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 
"""
global pi
pi = 3.141617  # immutable - when global, call by reference
details = {  # mutable
    'lang': 'Python',
}

print('id(pi)', id(pi))

def simple_function():
    global pi
    print("Inside function call, pi", pi, "details", details)
    pi = 78
    details['lang'] = 'clojure'
    print("Before function exit, pi", pi, "details", details)
    print('id(pi)', id(pi))


print("before function call, pi", pi, "details", details)
simple_function()
print("after function call, pi", pi, "details", details)

print('id(pi)', id(pi))
