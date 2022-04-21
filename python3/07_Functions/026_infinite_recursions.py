#!/usr/bin/python3
"""
Purpose: Infinite recursions
"""
import sys


def display(name):
    print(name)
    return display(name)


# display("Udhay")
# RecursionError: maximum recursion depth exceeded while calling a Python object

# To get the stack depth - platform dependent
print(f"{sys.getrecursionlimit() =}")  # 1000
# NOTE: By default, its limit is 1000 in script mode & 3000 in interactive mode

# To set the recursion limit
sys.setrecursionlimit(1500)

print(f"{sys.getrecursionlimit() =}")  # 1500


# display("Udhay")
# RecursionError: maximum recursion depth exceeded while calling a Python object


# ----------------------------------------


def loop(no_of_recursions):
    no_of_recursions += 1
    print(f"This is recursion number {no_of_recursions}")
    return loop(no_of_recursions)


# loop(no_of_recursions=0)
# RecursionError: maximum recursion depth exceeded while calling a Python object


# Mutual recursive Functions ==========================================

f1_count, f2_count = 0, 0


def func1():
    global f1_count
    f1_count += 1
    print(f"func1:{f1_count}")
    return func2()


def func2():
    global f2_count
    f2_count += 1
    print(f"\tfunc2:{f2_count}")
    return func1()


# func1()
# RecursionError: maximum recursion depth exceeded while calling a Python object

try:
    func1()
except RecursionError as ex:
    print(ex)
# func1:498
# func2:498

# func1:748
# func2:748
# maximum recursion depth exceeded while calling a Python object
