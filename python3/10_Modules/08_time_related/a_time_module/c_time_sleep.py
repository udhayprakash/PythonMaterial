#!/usr/bin/python
"""
Purpose: Calculating time taken for any logic
"""
import time


def time_taken(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f"\nTIME TAKEN{args}: {end_time - start_time} ns")
        return result

    return inner


@time_taken
def time_taking_function(num):
    time.sleep(num)


if __name__ == "__main__":
    print("Started! Sleeping for 10 seconds")
    time.sleep(10)
    print("I am back!! Sleeping 3 seconds")
    time.sleep(3)
    print("I am back Again!!!")

    time_taking_function(1)
    time_taking_function(2)
    time_taking_function(12)
