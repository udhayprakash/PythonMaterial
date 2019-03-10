#!/usr/bin/python
__author__ = 'udhay prakash'
"""
Problem 1: Return the fibonacci series (0, 1, 1, 2, 3, 5, 8) 
           using recursions
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

# 5th element    # fib(4)+fib(3)
                 # fib(4) -> fib(3)+fib(2);
                        # fib(3) -> fib(2)+fib(1)
                                    # fib(2) -> fib(1)+ fib(0) = 1+ 0
                 #             fib ...
print(fib(5))

# print '='*80
# factorial(5) = 5*4*3*2*1 =


def factorial(n):
    if n == 0:
        return 1
    else:
        return abs(n) * factorial(abs(n)-1)

print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(5))

print(factorial(-5))



print('='*80)





# # Infinite loop between these functions  --- Mutual recursion
# def func1():
#     print 'I am in function 1 .'
#     return func2()

# def func2():
#     print 'I am in function 2 .'
#     return func1()

# func1()

# '''
# **NOTE :**
# - Python doesnot have Tail Call optimization(TCO), to handle the recursive functions.
# - It is very difficult to add TCO to python, as it is a dynamic language.
# '''
