#!/usr/bin/python3
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
            yield num  # 2, 4, 6, 8, 10

def multiply_by_three(nums):
    print('multiply_by_three - start')
    for num in nums:
        yield num * 3  # 6, 12, 18, 24, 30

def convert_to_string(nums):
    print('convert_to_string - start')
    for num in nums:
        yield f'Number:{num}'


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# problem
print(list(even_filter(numbers)))
print(list(multiply_by_three(numbers)))
print(list(convert_to_string(numbers)))

# solution
pipeline = convert_to_string(
            multiply_by_three(even_filter(numbers))
)

print(pipeline)

print(f'{next(pipeline) = }')


for each in pipeline:
    print(each)