#!/usr/bin/python3
"""
Purpose: Higher-Order Functions
    - function which were designed to work on another functions
        - zip, map, filter, reduce
"""
# Method 1
odd_nums = []
for num in range(9):
    if num % 2:
        odd_nums.append(num)

print(odd_nums)

# Method 2: list comprehension
odd_nums1 = [num for num in range(9) if num % 2]
print(odd_nums1)

# Method 3: applying functions
def is_odd(n):
    return True if n % 2 else False


odd_nums2 = []
for num in range(9):
    if is_odd(num):
        odd_nums2.append(num)

print(odd_nums2)

# Method 4: applying functions
odd_nums3 = list(map(is_odd, range(9)))
print(odd_nums3)

odd_nums3 = list(filter(is_odd, range(9)))
print(odd_nums3)
print()

# Method 4: applying lambdas
odd_nums3 = list(map(lambda x: x % 2 != 0, range(9)))
print(odd_nums3)

odd_nums3 = list(filter(lambda x: x % 2 != 0, range(9)))
print(odd_nums3)

"""
Assignment:
----------
1) Try to get the prime numbers between 1208 and 4893
    HINTS: used-defined function to check primeness of a number
           filter()
"""
