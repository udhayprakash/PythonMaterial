#!/usr/bin/python
"""
Purpose:
Write a function that takes in a non-empty array of distinct integers 
and an integer representing a target sum. If any two numbers in the 
input array sum up to the target sum, the function should return them 
in an array, in sorted order. If no two numbers sum up to the target sum, 
the function should return an empty array. Assume that there will be at 
most one pair of numbers summing up to the target sum.


"""


def twoNumberSum(array, targetSum):
    pass


print(twoNumberSum([4, 6], 10))

# assert twoNumberSum([4, 6], 10), [4, 6])
# assert twoNumberSum([4, 6, 1], 5), [1, 4])
# assert twoNumberSum([4, 6, 1, -3], 3), [-3, 6])
# assert twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])
# assert twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17), [8, 9])
# assert twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18), [3, 15])
# assert twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5), [-5, 0])
# assert twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163), [-47, 210])
# assert twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164), [])
# assert twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15), [])
