#!/usr/bin/python3
"""
Purpose: Leap Year Checks

Algorithms
-----------
    if (year is not divisible by 4) then (it is a common year)
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)

    Compute the leap years in this century
"""
import calendar

year = 2021

# Method 1
if year % 4:  # != 0:
    print(f"year {year} is a common year")
elif year % 100:  # != 0
    print(f"year {year} is a LEAP year")
elif year % 400:
    print(f"year {year} is a common year")
else:
    print(f"year {year} is a LEAP year")

# Method 2
print(f"{calendar.isleap(year) =}")
if calendar.isleap(year):
    print(f"year {year} is a LEAP year")
else:
    print(f"year {year} is a common year")

# To generate all years in this century
for year in range(2000, 2101):
    print(year)

# Assignment: Join the for loop and conditonal
# logic to print the results
