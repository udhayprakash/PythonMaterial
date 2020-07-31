#!/usr/bin/python
"""
Purpose: program to display all the 
       prime numbers within an interval
"""

lower = 90
upper = 450

lower = int(input('Enter the lower bound:'))
upper = int(input('Enter the upper bound:'))

print(f'Prime numbers between {lower} and {upper} are:')

for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for factor in range(2, num):
            if (num % factor) == 0:
                # print(f'\t{num =:3} {factor =:2}') # {num % factor = }')
                break
        else:
            print(f'{num:3} is a prime number')
