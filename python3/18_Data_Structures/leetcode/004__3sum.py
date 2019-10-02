#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/3sum/
"""
import time


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        result = []
        for ech in list(combinations(nums, 3)):
            if not sum(ech):
                result.append(ech)
        return result
        # groups = []
        # for _index, ech in enumerate(nums):
        #     print(nums[_index+1:])
        #     for _index2, ech2 in enumerate(nums[_index+1:]):
        #         # print(_index2, ech2)
        #         # print([ech, ech2, *nums[_index+1:][_index2+1:_index2+2]])
        #         temp_list =  sorted([ech, ech2, *nums[_index+1:][_index2+1:_index2+2]])
        #         if not temp_list in groups and len(temp_list) == 3 and sum(temp_list) == 0: 
        #             groups.append(temp_list)
        # return groups


s = Solution()
# print(s.threeSum([-2,0,1,1,2]))
start_time = time.time_ns()
s.threeSum(
    [-15, 10, 0, -2, 14, -1, -10, -14, 10, 12, 6, -6, 10, 2, -11, -9, 2, 13, 2, -9, -14, -12, -10, -12, 13, 13, -10, -3,
     2, -11, 3, -6, 6, 10, 7, 5, -13, 4, -2, 12, 1, -11, 14, -4, 6, -12, -6, -14, 8, 11, -8, 1, 7, -3, 5, 5, -13, 10, 9,
     -3, 6, -10, 6, -3, 7, -9, -13, 9, 10, 0, -1, -11, 4, -10, -8, -13, -15, 2, -12, 8, -2, -12, -14, -10, -8, 6, 2, -5,
     -7, -11, 7, 14, -6, -10, -12, 8, -4, -10, -5, 14, -3, 9, -12, 8, 14, -13])
print(time.time_ns() - start_time)
# print()             # 0 1 2 3 4
# for i in s.threeSum([-2,0,1,1,2]):
#     print(i)

# -2,0,1,1,2
# -2,1,1,2,0
# -2,1,2,0,1
# -2,2,0,1,1
# -2,0,1,1,2

# original_list = [-2,0,1,1,2]
# for _index, ech in enumerate(original_list):
#     del original_list[_index]
#     mytuple =  tuple(original_list)  #[_index +1:]  
#     i = 0
#     while i < len(mytuple):
#         mytuple = (mytuple[-1],) + mytuple[:-1]
#         combinations = (ech,) + mytuple
#         for each_c in combinations:

#         i += 1


# -2,0,1
# -2,1,1
# -2,1,2   
# -2, 2, 0  =====
# -2,0,1,1,2
# -2,0,1,1,2

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


# def all_subsets(di, i) :
#     ret = []
#     for j, item in enumerate(di) :
#         if i == 1 :
#             ret = [(j,) for j in di]
#         elif len(di) - j >= i :
#             for subset in all_subsets(di[j + 1:], i - 1) :
#                 if sum((item,) + subset) == 0:
#                     print((item,) + subset)
#                     ret.append((item,) + subset)
#     return ret

# def all_subsets_gen(di, i) :
#     for j, item in enumerate(di) :
#         if i == 1 :
#             yield (j,)
#         elif len(di) - j >= i :
#             for subset in all_subsets(di[j + 1:], i - 1) :
#                 yield (item,) + subset

# start_time = time.time_ns()
# set(all_subsets_gen([-15,10,0,-2,14,-1,-10,-14,10,12,6,-6,10,2,-11,
# -9,2,13,2,-9,-14,-12,-10,-12,13,13,-10,-3,2,-11,3,-6,6,10,7,5,
# -13,4,-2,12,1,-11,14,-4,6,-12,-6,-14,8,11,-8,1,7,-3,5,5,-13,10,
# 9,-3,6,-10,6,-3,7,-9,-13,9,10,0,-1,-11,4,-10,-8,-13,-15,2,-12,8,
# -2,-12,-14,-10,-8,6,2,-5,-7,-11,7,14,-6,-10,-12,8,-4,-10,-5,14,-3,9,-12,8,14,-13], 3))
# print(time.time_ns()- start_time)

from itertools import permutations, combinations

print(list(permutations('ABC')))
print()
print(list(permutations([-2, 0, 1, 1, 2], 3)))
# print()
# print(list(combinations([-2,0,1,1,2])))
