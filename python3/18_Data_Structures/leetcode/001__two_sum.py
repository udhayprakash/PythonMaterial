#!/usr/bin/python
"""
Purpose: 
    https://leetcode.com/problems/two-sum/

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        input : nums: List[int], target: int
        output: List[int]
        """
        for ech_num in nums:
            for next_num in nums[nums.index(ech_num) + 1:]:
                if ech_num + next_num == target:
                    return [nums.index(ech_num), nums.index(next_num, nums.index(ech_num) + 1)]

    def twoSum(self, nums, target):
        """
        input : nums: List[int], target: int
        output: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index
        return []


s = Solution()
# s.twoSum(eval(input()), 9)

assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], 6) == [1, 2]
assert s.twoSum([3, 3], 6) == [0, 1]
assert s.twoSum([3, 2, 3], 6) == [0, 2]
assert s.twoSum([0, 4, 3, 0], 0) == [0, 3]
assert s.twoSum([-3, 4, 3, 90], 0) == [0, 2]
'''
2, 7, 11, 15

2, 7
2, 11
2, 15

7, 11
7, 15, 

11, 15
'''
