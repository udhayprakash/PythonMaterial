#!/usr/bin/python
"""
Purpose: sys module 
"""
import sys 

my_int = 12323 # int 
print(f'{my_int.__sizeof__()  =}')
print(f'{sys.getsizeof(my_int)=}')

my_float = 123.23 # float 
print(f'{my_float.__sizeof__()  =}')
print(f'{sys.getsizeof(my_float)=}')

my_none = None # None Type
print(f'{my_none.__sizeof__()  =}')
print(f'{sys.getsizeof(my_none)=}')

my_bool = True  # bool
print(f'{my_bool.__sizeof__()  =}')
print(f'{sys.getsizeof(my_bool)=}')

my_str = 'Python' # str
print(f'\n{my_str.__sizeof__()   =}')
print(f'{sys.getsizeof(my_str) =}')

my_list = [12, 123, 23] # list
print(f'\n{my_list.__sizeof__()   =}')
print(f'{sys.getsizeof(my_list) =}')


my_tuple = (12, 123, 23) # tuple
print(f'\n{my_tuple.__sizeof__()   =}')
print(f'{sys.getsizeof(my_tuple) =}')

my_set = {12, 123, 23} # set
print(f'\n{my_set.__sizeof__()   =}')
print(f'{sys.getsizeof(my_set) =}')