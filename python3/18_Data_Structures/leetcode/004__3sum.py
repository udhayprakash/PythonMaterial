#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/3sum/
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        groups = []
        for _index, ech in enumerate(nums):
            for _index2, ech2 in enumerate(nums[_index+1:]):
                # print([ech, ech2, *nums[_index+1:][_index2+1:_index2+2]])
                temp_list =  sorted([ech, ech2, *nums[_index+1:][_index2+1:_index2+2]])
                if not temp_list in groups and len(temp_list) == 3 and sum(temp_list) == 0: 
                    groups.append(temp_list)
        return groups

s = Solution()


print()
for i in s.threeSum([-2,0,1,1,2]):
    print(i)
-2,0,1
-2,1,1
-2,1,2
-2,0,1,1,2
-2,0,1,1,2

# print()
# for i in s.threeSum([-1,0,1,0]):
#     print(i)


# for i in s.threeSum([-1, 0, 1, 2, -1, -4]):
#     print(i)


# -1, 0, 1
# -1, 1, 2
# -1, 2, -1
# -1, -1, -4

# 0, 1, 2
# 0, 2, -1
# 0, -1, -4

# 1, 2, -1
# 1, -1, -4  ====

# 2, -1, -4