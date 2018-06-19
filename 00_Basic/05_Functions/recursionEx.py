#!/usr/bin/python
"""
Purpose: 


Three Laws of Recursion:
------------------------
1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.
"""


# calculating sum of a list of numbers

def sumOfList(numList):  # conventional implementation
    total = 0
    for i in numList:
        total += i
    return total


print sumOfList([12, 23, 34, 546, 1])


def sumOfListRec(numList):  # implementation using recursions
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sumOfListRec(numList[1:])


print sumOfListRec([12, 23, 34, 546, 1])

"""
exercises on recursions:
--------------------------
1. Write a recursive function to compute the factorial of a number
2. Write a recursive function to reverse a list
3. Write a recursive function to compute the fibonacci series
"""
