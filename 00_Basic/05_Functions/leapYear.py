#!/usr/bin/python
"""
Purpose: Script to check whether a year is LEAP YEAR or not.

In the Gregorian calendar three criteria must be taken into account to identify leap years:

    The year can be evenly divided by 4, is is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

Leap Years from 1900:
	1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960,
	1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020
"""


def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap


if __name__ == '__main__':
    years = xrange(1900, 2000)
    for y in years:
        print y, is_leap(y)

