#!/usr/bin/python
"""
Purpose: Fibonacci series Generation 
    - first two numbers are 0 & 1
    - each next number is a summation of previous two nums 
    - 0, 1, 1, 2, 3, 5, 8, 13, .....

 (0, 1, 1, 2, 3, 5, 8, 13....) 
  0  1  2  3  4  5  6   7 
           using recursions
"""
def fib(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(f'{fib(5) =}')
# fib(4)                                + fib(3)
# fib(3)            + fib(2)            + fib(2)            + fib(1)
# fib(2) + fib(1)   + fib(1) + fib(0)   + fib(1) + fib(0)   + fib(0) + fib(-1) ...

print(f'{fib(6) =}')

for loop_index, num in enumerate(range(5)):
    print(f'{loop_index:2} th element is {fib(num):4}')


# Method 2
def get_fibs_till(n):
    a, b = 0, 1
    fib_nums = []
    for _ in range(n):
        a, b = b, a+ b
        fib_nums.append(a)
    return fib_nums


print('first 5 fib series nums:', get_fibs_till(5))


'''
**NOTE :**
- Python doesnot have Tail Call optimization(TCO), to handle the recursive functions.
- It is very difficult to add TCO to python, as it is a dynamic language.
'''
