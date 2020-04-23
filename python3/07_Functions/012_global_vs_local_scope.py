#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 

call by value 
    - changes within the function will NOT reflect at the global level 

call by reference 
    - changes within the function will reflect at the global level 

immutable objects - int, float, None, bool, tuple, string, frozenset
mutable objects - list, set, dict, bytearray string

NOTE:
-----
mutable object can be edited within function without passing as args
immutable object CANT be edited within function without passing as args
"""
pi = 3.141  # immutable - call by value

# case 1============
def simple_function():
    print('pi = {}'.format(pi))
    print('pi = {}'.format(pi * 12))


simple_function()

# case 2 ==================
def simple_function():
    print('before change pi = {}'.format(pi))
    pi = 3333333
    print('after  change pi = {}'.format(pi))


simple_function()
# # UnboundLocalError: local variable 'pi' referenced before assignment


# case 3=====   call by value
def simple_function(pi):
    print('before change pi = {}'.format(pi))
    pi = 3333333
    print('after  change pi = {}'.format(pi))


simple_function(pi)
print('outside function pi = {}'.format(pi))
# # NOTE: changes with in function are not reflected outside it.

# case 4=====   call by reference
def simple_function(pi):
    global pi
    print('before change pi = {}'.format(pi))
    pi = 3333333
    print('after  change pi = {}'.format(pi))

simple_function(pi) # SyntaxError: name 'pi' is parameter and global
print('outside function pi = {}'.format(pi))

# case 5=====   call by reference
def simple_function():
    global pi
    print('before change pi = {}'.format(pi))
    pi = 3333333
    print('after  change pi = {}'.format(pi))


simple_function()
print('outside function pi = {}'.format(pi))

# NOTE: For immutable objects, default is call by value.
# when global keyword is used, it will become call by reference.


##############################################
details = {  # mutable - call by reference
    'ver': '3.7.0'
}


# case 6=====   call by reference
def simple_function():
    print(f'\nbefore change ver = {details["ver"]}')
    details['ver'] = '3.8'
    print(f'before change ver = {details["ver"]}')


simple_function()
print('outside function ver = {}'.format(details['ver']))
