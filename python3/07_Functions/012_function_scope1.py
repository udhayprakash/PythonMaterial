#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 

call by value 
    - changes within the function will NOT reflect at the global level 

call by reference 
    - changes within the function will reflect at the global level 

"""
pi = 3.141  # immutable - call by value
details = {  # mutable - call by reference
    'ver': '3.7.0'
}

# print('id(pi)', id(pi))

def simple_function():
    """
    mutable object can be edited within function without passing as args
    immutable object CANT be edited within function without passing as args
    """
    # print('Inside func. call, pi', pi)
    pi = 78 # UnboundLocalError: local variable 'pi' referenced before assignment
    details['ver'] = '3.8.1'
    print("Inside func. call, pi", pi, "details", details)
    # print('id(pi)', id(pi))


print("before func. call, pi", pi, "details", details)
simple_function()
print("after func. call, pi", pi, "details", details)

