#!/usr/bin/python3
"""
Purpose: Decorator for time taken
"""
import time

start_time = time.perf_counter_ns()
# logic
for _ in range(1000):
    pass

# Method 1
end_time = time.perf_counter_ns()
print(end_time - start_time)

# Method 2
print(time.perf_counter_ns() - start_time)


# ======== TIME TAKEN CALCULATION DECORATOR
def time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f"Time Taken for {func.__name__}: {end_time - start_time} ns")
        return result

    return wrapper


@time_taken
def my_func(num):
    for _ in range(num):
        pass
    print(f"for {num:5} numbers", end=":->")


my_func(78)
my_func(900)
my_func(9000)


@time_taken
def f1():
    elements = [1] * 10_000
    for _ in range(len(elements)):
        elements.pop()


@time_taken
def f2():
    elements = [1] * 10_000
    for _ in range(len(elements)):
        elements.pop(0)


f1()  # 1170200 ns
f2()  # 8369400 ns
