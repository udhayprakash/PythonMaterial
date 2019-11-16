#!/usr/bin/python
"""
Purpose: decorator example
"""
import time


def time_taken(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter_ns()
        func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f'Time Taken: {end_time - start_time} ns')

    return inner


def print_function(func):
    def wrapper(*args, **kwargs):
        print(f'\n{func.__name__} func - Start')
        func(*args, **kwargs)
        print(f'{func.__name__} func - before close')

    return wrapper


@print_function
@time_taken
def my_func(num):
    for i in range(num):
        pass


my_func(9000)
my_func(78)
