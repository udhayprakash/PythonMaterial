#!/usr/bin/python
"""
Purpose: Leap Year Checks

Algorithms
-----------
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)

"""


import calendar

for year in range(1000, 2100):
    # Method 1
    if year % 4:
        print(f'year {year} is a common year')
    elif year % 100:
        print(f'year {year} is a LEAP year')
    elif year % 400:
        print(f'year {year} is a common year')
    else:
        print(f'year {year} is a LEAP year')

    # Method 2
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f'year {year} is a LEAP year')
            else:
                print(f'year {year} is a common year')
        else:
            print(f'year {year} is a LEAP year')
    else:
        print(f'year {year} is a common year')

    # Method 3
    if calendar.isleap(year):
        print(f'year {year} is a LEAP year')
    else:
        print(f'year {year} is a common year')
    print()
