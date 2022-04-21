#!/usr/bin/python3
"""
Purpose: Decorator with arguments
"""
import time


def decorator(arg1, arg2):
    def inner_function(function):
        def wrapper(*args, **kwargs):
            print(f'Arguments passed to decorator are {arg1} and{arg2}')
            print(f'Function arguments are {args}')
            function(*args, **kwargs)

        return wrapper

    return inner_function


@decorator('arg1', 'arg2')
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3)
print()


# ===============================
def time_taken(metric):
    def inner(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter_ns()
            result = func(*args, **kwargs)
            end_time = time.perf_counter_ns()
            if metric == 'ms':
                print(f'Time Taken: {(end_time - start_time) / 1000} ms')
            else:
                print(f'Time Taken: {end_time - start_time} ns')
            return result

        return wrapper

    return inner


@time_taken('ms')
def my_func(num):
    for _ in range(num):
        pass
    print(f'for {num:5} numbers', end=':->')


my_func(78)
my_func(900)
my_func(9000)
