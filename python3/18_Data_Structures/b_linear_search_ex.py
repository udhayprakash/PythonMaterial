#!/usr/bin/python
"""
Purpose: Linear Search Implemenation 
"""
import time


# linear search - O(n)
# pythonic way 

def linear_search_pythonic(given_list, search_ele):
    # return given_list.count(search_ele) != 0
    return search_ele in given_list


def linear_search(given_list, search_ele):
    """
    This is faster than pythonic way
    """
    for each_chr in given_list:
        if each_chr == search_ele:
            return True
    return False


start_time = time.perf_counter()
print(linear_search_pythonic([1, 2, 3, 4, 6, 7, 8, 9], 5))
print(time.perf_counter() - start_time)

start_time = time.perf_counter()
print(linear_search([1, 2, 3, 4, 6, 7, 8, 9], 5))
print(time.perf_counter() - start_time)
