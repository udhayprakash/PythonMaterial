#!/usr/bin/python
"""
Purpose: decorator example
"""
def decortor_func1(func):
    def wrapper(*args, **kwargs):
        print(' I am  in decorator 1')
        func(*args, **kwargs)
    return wrapper

def decortor_func2(func):
    def wrapper(*args, **kwargs):
        print(' I am  in decorator 2')
        func(*args, **kwargs)
    return wrapper


@decortor_func2
@decortor_func1
def actual_function():
    print('I am actual functioon')


actual_function()