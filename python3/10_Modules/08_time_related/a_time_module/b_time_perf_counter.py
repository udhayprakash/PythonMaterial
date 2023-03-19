#!/usr/bin/python
"""
Purpose: Calculating time taken for any logic
"""
import time

# Method 1 - Implementing in each function
# def factorial(num):
#     start_time = time.perf_counter() # time_ns()
#     result = 1
#     for i in range(1, num):
#         result *= i
#     print('TIME TAKEN', time.perf_counter() - start_time, end = "\n\n")
#     return result


# print(factorial(7))  # 720
# print(factorial(77))  # 1885494701666050254987932260861146558230394535379329335672487982961844043495537923117729972224000000000000000000


# def get_even_nums(n):
#     start_time = time.perf_counter() # time_ns()
#     evens = []
#     for num in range(n):
#         if num % 2 == 0:
#             evens.append(num)
#     print('TIME TAKEN', time.perf_counter() - start_time, end = "\n\n")
#     return evens


# print(get_even_nums(10))
# print(get_even_nums(100))


# METHOD 2 - creating a decorator, and reusing
print()


def time_taken(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()  # time_ns()
        result = func(*args, **kwargs)
        print("TIME TAKEN", time.perf_counter() - start_time, end="\n\n")
        return result

    return inner


@time_taken
def factorial(num):
    result = 1
    for i in range(1, num):
        result *= i
    return result


print(factorial(7))  # 720
print(
    factorial(77)
)  # 1885494701666050254987932260861146558230394535379329335672487982961844043495537923117729972224000000000000000000


@time_taken
def get_even_nums(n):
    evens = []
    for num in range(n):
        if num % 2 == 0:
            evens.append(num)
    return evens


print(get_even_nums(10))
print(get_even_nums(100))
