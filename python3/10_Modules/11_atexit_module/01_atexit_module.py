#!/usr/bin/python
"""
Purpose: atexit
    - Call functions when a program is closing down
"""
import atexit


def hello():
    print("Hello world")


def add(n1, n2):
    print("add - function")
    return n1 + n2


def all_done():
    print("all_done()")


print("Registering")
atexit.register(all_done)
print("Registered")


if __name__ == "__main__":
    hello()
    # print(dir(atexit))
    # all_done()

    res = add(10, 20)
    print(f"{res = }")
