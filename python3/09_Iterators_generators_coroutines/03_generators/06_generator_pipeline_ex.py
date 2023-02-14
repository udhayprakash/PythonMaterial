#!/usr/bin/python3
"""
Purpose:
    Problem statement
        - For given numbers
            - Filter even number
            - multiply by three
            - convert to string
"""


# Method 1
def even_filter(nums):
    print("even_filter - start")
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def multiply_by_three(nums):
    print("multiply_by_three - start")
    muls_of_3 = []
    for num in nums:
        muls_of_3.append(num * 3)

    return muls_of_3


def convert_to_string(nums):
    print("convert_to_string - start")
    num_strs = []
    for num in nums:
        num_strs.append(f"Number:{num}")

    return num_strs


result = convert_to_string(multiply_by_three(even_filter(numbers)))
print(f"{result = }")


# Method 2
def even_filter(nums):
    print("even_filter - start")
    for num in nums:
        if num % 2 == 0:
            yield num


def multiply_by_three(nums):
    print("multiply_by_three - start")
    for num in nums:
        yield num * 3


def convert_to_string(nums):
    print("convert_to_string - start")
    for num in nums:
        yield f"Number:{num}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Problem
print(f"{list(even_filter(numbers))       =}")  # [2, 4, 6, 8, 10]
print(f"{list(multiply_by_three(numbers)) =}")  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(
    f"{list(convert_to_string(numbers)) =}"
)  # ['Number:1', 'Number:2', 'Number:3', 'Number:4', 'Number:5', 'Number:6', 'Number:7', 'Number:8', 'Number:9', 'Number:10']

# Solution
pipeline = convert_to_string(multiply_by_three(even_filter(numbers)))
print(pipeline)  # <generator object convert_to_string at 0x000001BDA70E60A0>

print(f"{next(pipeline) = }")  # 'Number:6'

for each in pipeline:
    print(each)

# Number:12
# Number:18
# Number:24
# Number:30
