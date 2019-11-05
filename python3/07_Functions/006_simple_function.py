#!/usr/bin/python
"""
Purpose: WAP to display the addition of given values
"""


def addition(num1, num2, num3):
    result = num1 + num2 + num3
    return result


print(addition(12, 13, 14))
result = addition(12, 13, 14)
print(result)

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

'''
Assignment
----------
1) write a function to mimick the sum() function.
Caution: don't create function with same name

2)write a function to implement the following:
    - input: ((1,2), 3,4, (5, 6))
    - output: (1, 2, 3, 4, 5, 6)
'''
