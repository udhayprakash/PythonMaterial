#!/usr/bin/python3
"""
Purpose: Decorator for time taken
"""
import time

start_time = time.perf_counter_ns()
end_time = time.perf_counter_ns()

# print(end_time - start_time)
print(time.perf_counter_ns() - start_time)


def time_taken(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter_ns()
        func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f'Time Taken: {end_time - start_time} ns')

    return inner

@time_taken
def my_func(num):
    for _ in range(num):
        pass
    print(f'\nfor {num} numbers')

my_func(78)
my_func(900)
my_func(9000)
