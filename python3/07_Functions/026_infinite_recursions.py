#!/usr/bin/python
"""
Purpose: INfinite recursions 
"""
import sys 

def display(name):
    print(name)
    return display(name)


# To get the stack depth - platform dependent
print(f'{sys.getrecursionlimit() =}')  # 1000 
# NOTE: By default, its limit is 1000 in script mode & 2000 in interactive mode

sys.setrecursionlimit(1500)
print(f'{sys.getrecursionlimit() =}')  # 1000 

# display('Udhay')
# RecursionError: maximum recursion depth exceeded while calling a Python object

no_of_recursions = 0

# Infinite Loop 
def loop(no_of_recursions):
    no_of_recursions += 1
    print(f'This is recursion number {no_of_recursions}')
    return loop(no_of_recursions)

# loop(no_of_recursions)
# RecursionError: maximum recursion depth exceeded while calling a Python object


# Mutual recursive Functions 
def func1():
    print('func1')
    return func2()

def func2():
    print('func2')
    return func1()

# func1()
# RecursionError: maximum recursion depth exceeded while calling a Python object