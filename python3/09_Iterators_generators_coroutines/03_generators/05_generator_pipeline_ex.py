#!/usr/bin/python
"""
Purpose: 
    Problem statement 
        - For given numbers 
            - Filter even number 
            - multiply by three 
            - convert to string
"""

def even_filter(nums):
    print('even_filter - start')
    for num in nums:
        if num % 2 == 0:
            yield num   # 2, 4, 6, ...


def multiply_by_three(nums):
    print('multiply_by_three - start')
    for num in nums:
        yield num * 3   # 6, 12, 18, ....


def convert_to_string(nums):
    print('convert_to_string - start')
    for num in nums:
        yield '\tThe Number: %s' % num    


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(multiply_by_three(even_filter(nums)))

print(pipeline)  # <generator object convert_to_string at 0x000002BD57CF2F20>

print(next(pipeline))
print(next(pipeline))

for each in pipeline:
    print(each)
