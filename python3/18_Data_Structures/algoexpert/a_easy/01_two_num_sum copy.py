#!/usr/bin/python
"""
Purpose: 
You're given an array of integers. Write a function that returns a pair of numbers such that they sum up to zero.

You can assume there will be exactly 1 solution. Each element in the array can only be used once.

ex:
Array of integers is [2, 7, 9, -2].
The pair that sums up to 0 is (2, -2).
"""


def pairOfZeroSum(nums):
    """
	Args:
		{List<int>} nums
	Returns:
		{List<int>} 2 numbers from nums that add up to 0.
	"""
    nums = nums + [nums[0]]
    for _index1, _ in enumerate(nums):
        val = nums[_index1:_index1 + 2]
        if not sum(val):
            return val


assert pairOfZeroSum([2, 7, 9, -2]) == [-2, 2]
