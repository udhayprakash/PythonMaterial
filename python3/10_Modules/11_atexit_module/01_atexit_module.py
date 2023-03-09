#!/usr/bin/python
"""
Purpose: atexit
    - Call functions when a program is closing down
"""

import atexit


def add(n1, n2):
    print("add - function")
    return n1 + n2


def all_done():
    print("all_done()")


# all_done()

print("Registering")
atexit.register(all_done)
print("Registered")


res = add(10, 20)
print(f"{res = }")
