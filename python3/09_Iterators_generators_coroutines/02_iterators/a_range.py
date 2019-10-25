#!/usr/bin/python
"""
Purpose:  range() type
"""

nums = range(9)  
# optimized object - Lazy loading

print(f'nums: {nums}, {type(nums)}')

# iterating on range object 
for each_val in nums:
    print(each_val)


# Convert to other iterables
nums1 = list(nums)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(f'nums1: {nums1}, {type(nums1)}')

nums2 = tuple(nums) # (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(f'nums2: {nums2}, {type(nums2)}')

nums3 = set(nums)  # {0, 1, 2, 3, 4, 5, 6, 7, 8}
print(f'nums3: {nums3}, {type(nums3)}')

nums4 = str(nums)  # range(0, 9),
print(f'nums4: {nums4}, {type(nums4)}')

