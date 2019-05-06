#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 

call by value 
    - changes within the function will NOT reflect at the global level 

call by reference 
    - changes within the function will reflect at the global level 

immutable objects - int, float, None, bool, tuple, string
mutable objects - list, set, dict, bytearray string
"""
pi = 3.141  # immutable - call by value

# # case 1============
# def simple_function():
#     print('pi = {}'.format(pi))
#     print('pi = {}'.format(pi* 12))

# simple_function()

# # case 2 ==================
# def simple_function():
#     print('before change pi = {}'.format(pi))
#     pi = 3333333
#     print('after  change pi = {}'.format(pi))

# simple_function()
# # UnboundLocalError: local variable 'pi' referenced before assignment

# # case 3=====   call by value
# def simple_function(pi):
#     print('before change pi = {}'.format(pi))
#     pi = 3333333
#     print('after  change pi = {}'.format(pi))

# simple_function(pi)
# print('outside function pi = {}'.format(pi))
# changes with in function are not reflected outside it

# case 3=====   call by reference
# def simple_function(pi):
#     global pi
#     print('before change pi = {}'.format(pi))
#     pi = 3333333
#     print('after  change pi = {}'.format(pi))

# simple_function(pi) # SyntaxError: name 'pi' is parameter and global
# print('outside function pi = {}'.format(pi))

# def simple_function():
#     global pi
#     print('before change pi = {}'.format(pi))
#     pi = 3333333
#     print('after  change pi = {}'.format(pi))

# simple_function() 
# print('outside function pi = {}'.format(pi))


details = {  # mutable - call by reference
    'ver': '3.7.0'
}

def simple_function():
    print('before change ver = {}'.format(details['ver']))
    details['ver'] = '3.8'
    print('after  change ver = {}'.format(details['ver']))

simple_function() 
print('outside function ver = {}'.format(details['ver']))








# # print('id(pi)', id(pi))

# def simple_function():
#     """
#     mutable object can be edited within function without passing as args
#     immutable object CANT be edited within function without passing as args
#     """
#     # print('Inside func. call, pi', pi)
#     pi = 78 # UnboundLocalError: local variable 'pi' referenced before assignment
#     details['ver'] = '3.8.1'
#     print("Inside func. call, pi", pi, "details", details)
#     # print('id(pi)', id(pi))


# print("before func. call, pi", pi, "details", details)
# simple_function()
# print("after func. call, pi", pi, "details", details)

