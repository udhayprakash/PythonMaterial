#!/usr/bin/python
__author__ = 'udhay prakash'
"""
Problem 1: Return the fibonacci series
 (0, 1, 1, 2, 3, 5, 8, 13....) 
  0  1  2  3  4  5
           using recursions
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 5th element    # fib(4)+fib(3)
# fib(4) -> fib(3) + fib(2);
# fib(3) -> fib(2)+fib(1)
# fib(2) -> fib(1)+ fib(0) = 1+ 0
#             fib ...
# print(fib(5))

for loop_index, num in enumerate(range(20)):
    print(f'{loop_index:2} th element is {fib(num)}')


'''
**NOTE :**
- Python doesnot have Tail Call optimization(TCO), to handle the recursive functions.
- It is very difficult to add TCO to python, as it is a dynamic language.
'''
