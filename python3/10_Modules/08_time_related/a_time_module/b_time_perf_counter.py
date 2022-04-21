#!/usr/bin/python
"""
Purpose: Calculating time taken for any logic
"""
import time


# def time_taken(func):
#     def inner(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(f'\nTIME TAKEN: {end_time - start_time} sec')
#         return result
#     return inner


def time_taken(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f"\nTIME TAKEN: {end_time - start_time} ns")
        return result

    return inner


@time_taken
def factorial(num):
    result = 1
    for i in range(1, num):
        result *= i
    return result


print(f"{factorial(5) =}")
print(f"{factorial(50) =}")
