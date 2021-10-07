#!/usr/bin/python3
"""
Purpose: sys module 
"""
import sys 

my_int = 123 # int 
print(f'\n{my_int.__sizeof__()  =}') # 28
print(f'{sys.getsizeof(my_int)=}')

my_int = 12323123231232312323 # int 
print(f'\n{my_int.__sizeof__()  =}') # 36
print(f'{sys.getsizeof(my_int)=}')

my_float = 123.23 # float 
print(f'\n{my_float.__sizeof__()  =}') # 24
print(f'{sys.getsizeof(my_float)=}')

my_none = None # None Type
print(f'\n{my_none.__sizeof__()  =}')
print(f'{sys.getsizeof(my_none)=}')

my_bool = True  # bool
print(f'\n{my_bool.__sizeof__()  =}')
print(f'{sys.getsizeof(my_bool)=}')


my_str = 'Python' # str
print(f'\n{my_str.__sizeof__()   =}')
print(f'{sys.getsizeof(my_str) =}')

# ----------------
my_list = [12, 123, 23] # list
print(f'\n{my_list.__sizeof__()   =}') # 104
print(f'{sys.getsizeof(my_list) =}')   # 120


my_tuple = (12, 123, 23) # tuple
print(f'\n{my_tuple.__sizeof__()   =}')
print(f'{sys.getsizeof(my_tuple) =}')

my_set = {12, 123, 23} # set
print(f'\n{my_set.__sizeof__()   =}')
print(f'{sys.getsizeof(my_set) =}')
