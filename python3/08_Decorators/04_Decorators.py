#!/usr/bin/python
"""
Purpose: decorator example
"""
import time 

def time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        total = time.time() - start_time
        print(f'Function {func.__name__} took {total} seconds')
    return wrapper


@time_taken
def myfunc(num):
    for _ in range(num):
        pass


myfunc(1000)
myfunc(10000)
myfunc(100000)