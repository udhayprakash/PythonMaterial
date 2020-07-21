#!/usr/bin/python
"""
Purpose: To get all pronic numbers between 50 and 5000
"""

pronic_numbers = []
for num in range(50, 5000, 1):
    for i in range(1, num):
        if i * (i +1) == num:
            # print(f'{num} is a PRONIC number')
            pronic_numbers.append(num)
            break


print(pronic_numbers)