#!/usr/bin/python
"""
Purpose: Binary Search Implemenation 
"""
import time


# binary search 0(n/2)

def binary_search(given_list, search_ele):
    """
    Binary search expects the list to be in sorted order
    """
    while len(given_list) > 0:
        mid_value = len(given_list) // 2
        if given_list[mid_value] == search_ele:
            return True
        elif given_list[mid_value] < search_ele:
            given_list = given_list[:mid_value]
        else:
            given_list = given_list[mid_value + 1:]

    return False


start_time = time.perf_counter()
print(binary_search([1, 2, 3, 4, 6, 7, 8, 9], 5))
print(time.perf_counter() - start_time)

start_time = time.perf_counter()
print(binary_search([1, 2, 3, 4, 6, 7, 8, 9], 4))
print(time.perf_counter() - start_time)
