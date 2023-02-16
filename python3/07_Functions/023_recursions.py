#!/usr/bin/python3
"""
Purpose: Recursion
    - Recursion is a programming technique in which a call to a function results
       in another call to that same function.
    - Iteration is calling an object, and moving over it.


Three Laws of Recursion:
------------------------
    1. A recursive algorithm must have a base case.
    2. A recursive algorithm must change its state and move toward the base case.
    3. A recursive algorithm must call itself, recursively.

pseudo-code:
-------------
def funcName(<input paramaters>):
    <some condition check for termination>
    <some logic>
    return funcName(<input parameters>)


    ONLINE TOOL - https://www.recursionvisualizer.com/
"""


def hello():
    print("Hello")
    return hello()


hello()


# Example 1: Calculating sum of a list of numbers
# Method 1 : conventional implementation
def sum_of_list(num_list):
    total = 0
    for num in num_list:
        # total = total + num
        total += num
    return total


print(sum_of_list([12, 23, 34, 546, 1]))  # 616


# Method 2 : implementation using recursions
def sum_of_list_rec(num_list):
    if not num_list:
        return 0
    # print(f'{num_list = }')
    return num_list[0] + sum_of_list_rec(num_list[1:])


print(sum_of_list_rec([12, 23, 34, 546, 1]))  # 616

"""
[12, 23, 34, 546, 1]
12 + [23, 34, 546, 1]
12 + 23 + [34, 546, 1]
12 + 23 + 34 + [546, 1]
12 + 23 + 34 + 546 + [1]
12 + 23 + 34 + 546 + 1 + 0 # []
"""


def sum_of_list_rec(num_list):
    if len(num_list) == 1:
        return num_list[0]
    print(f"{num_list[0] = }\t {num_list[1:] =}")
    return num_list[0] + sum_of_list_rec(num_list[1:])


print(sum_of_list_rec([12, 23, 34, 546, 1]))

# Example 2: String reversal
"""
Python  # take first char and place at end
ythonP
thonPy
honPyt
onPyth
nPytho
"""


def string_reversal(word):
    if not word:
        return ""
    print(f"{word = }")
    return string_reversal(word[1:]) + word[0]


result = string_reversal("Python")
print(result)

# Python  # take last char and place at start
"""
nPytho
onPyth
honPyt
thonPy
....
"""


def string_reversal_1(word):
    if not word:
        return ""
    print(f"{word =}")
    return word[-1] + string_reversal_1(word[:-1])


result = string_reversal_1("Python")
print(result)
