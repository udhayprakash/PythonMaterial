"""
Purpose:
    1. Calculate factorial using recursion.
    2. Call factorial function using thread.
"""
from _thread import start_new_thread

my_thread_id = 1


def factorial(n):
    global my_thread_id
    if n < 1:  # base case
        print(f"Thread: {my_thread_id}")
        my_thread_id += 1
        return 1
    else:
        result = n * factorial(n - 1)  # recursive call
        print(f"{n} != {result}")
        return result


start_new_thread(factorial, (5,))
start_new_thread(factorial, (4,))

c = input("Waiting for threads to return...\n")
