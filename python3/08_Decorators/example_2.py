#!/usr/bin/python
"""
Purpose: Decaorator to calculate  the time taken by a function
"""
import time 



def display_exec_func_name(func):
    def wrapper(*args, **kwargs):
        print(f'Executing the function {func.__name__}')
        func(*args, **kwargs)
        print('Completed execution')
    return wrapper
    
@display_exec_func_name
def myfuntion():
    total = 0
    for each in range(9999):
        total += each 
    return total 

print(myfuntion())