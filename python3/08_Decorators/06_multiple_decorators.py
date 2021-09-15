#!/usr/bin/python
"""
Purpose: Decorator for time taken & print start/end together
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
    def inner(*args, **kwargs):
        print(f'\n\n{func.__name__} function - start ')
        result1 = func(*args, **kwargs)
        print(f'{func.__name__} function - before end')
        return result1

    return inner


@time_taken
@print_function
def my_func(num):
    for _ in range(num):
        pass
    print(f'\nfor {num} numbers')


my_func(78)
my_func(900)
my_func(9000)

# python execution order: top to bottom; left to right
