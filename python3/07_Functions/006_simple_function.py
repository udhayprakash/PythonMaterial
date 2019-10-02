#!/usr/bin/python
"""
Purpose: WAP to display the addition of given values
"""


def addition(num1, num2, num3):
    result = num1 + num2 + num3
    return result


print(addition(12, 13, 14))

# sum() - expects an iterable
# sum(12, 13, 14)
print(sum([12, 13, 14]))
print(sum((12, 13, 14)))
print(sum({12, 13, 14}))

# flattening a list of lists
mylist = [[1, 2], [3, 4], [5, 6]]
print(sum(mylist, []))

# mylist = [(1,2), [3,4], [5, 6]]
# print(sum(mylist, []))

mylist = [(1, 2), (3, 4), (5, 6)]
print(sum(mylist, ()))

mylist = ((1, 2), (3, 4), (5, 6))
print(sum(mylist, ()))

# mylist = ((1,2), 3,4, (5, 6))
# print(sum(mylist, ()))

# Assignment 
# func
#     - input: ((1,2), 3,4, (5, 6))
#     - ouput: (1, 2, 3, 4, 5, 6)
