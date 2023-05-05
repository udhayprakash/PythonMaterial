#!/usr/bin/python3
"""
Purpose: sys module
"""
import sys

num1 = 123
num2 = 123
num3 = 123

print(f"{sys.getrefcount(123) =}")
# NOTE: Returns how many variables are referring
# to this value
# Every number will have atleast 2 references


for i in range(800):
    print(f"{i} {sys.getrefcount(i)}")

print(f"{sys.getrefcount(-0.2) =}")
print(f"{sys.getrefcount(None) =}")
print(f"{sys.getrefcount(1)    =}")
print(f"{sys.getrefcount(True) =}")
print(f"{sys.getrefcount(0)    =}")
print(f"{sys.getrefcount(False)=}")

name = "Neha Rehman"
print(f'{sys.getrefcount("Neha Rehman")=}')  # 4

mylist = [45, 87, 23]
print(f"{sys.getrefcount([45, 87, 23])=}")
print()

a = {"hello": 42, "world": 99}
b = a

print("\nMoving on to some introspection of the object heap.")
# This is 3 instead of 2, because the getrefcount function has a local
# parameter variable pointing to the object received by the function.
print(f"The dictionary is referred to by {sys.getrefcount(a)} references.")
print(f"The dictionary size is {sys.getsizeof(a)} bytes.")

# The slack space in lists, sets and dictionaries makes modifications faster.
a["yeah"] = 12345
# The reported size does not change when adding new element.
print(f"After add, the dictionary size is still {sys.getsizeof(a)} bytes.")

print("\nObserve the growth of slack space at the end of a list.")
items = []
prev = sys.getsizeof(items)
print(f"Initial size of an entirely empty list is {prev} bytes.")
for i in range(10000):
    items.append(i)
    curr = sys.getsizeof(items)
    if curr != prev:
        print(f"At append #{i}, size increases by {curr - prev} bytes.")
        prev = curr

# Each list contains references to objects, but the objects themselves
# are not part of the list, but stored separately in the object heap.

big = list(range(1000000))
print(f"\nSize of the big list is {sys.getsizeof(big)} bytes.")
items.append(list)
print(f"After appending big list, new size is {sys.getsizeof(items)} bytes.")

# For homogeneous arrays of fixed size, the internal representation
# used by numpy is far more economical, at the price of flexibility.

import numpy as np

# Integers from range 0 to 1000000, each stored in exactly four bytes.
bign = np.arange(0, 1000000, dtype="uint32")
# This is 4000096, because of the info stored about numpy array
# itself, such as shape and element type.
print(f"Size of the numpy array is {sys.getsizeof(bign)} bytes.")

# Since string objects are immutable, Python stores them in a special way
# that allows it to reuse string literals instead of creating redundant
# copies of the same string content.
a = "Hello, yellow"
b = a
# This is 4 instead of 2, because of Python's internal reference, and
# the argument reference during the function call sys.getrefcount(a).
print(f"\nThe string object has {sys.getrefcount(a)} references.")  # 4
c = "Hello, yellow"
print(f"The string object has by {sys.getrefcount(a)} references.")  # 5
d = c[:]
print(f"The string object has {sys.getrefcount(a)} references.")  # 6
e = c[:5] + c[5:]
print(f"The string object has {sys.getrefcount(a)} references.")  # 6
