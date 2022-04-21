#!/usr/bin/python3
"""
Purpose: Demonstration of usage of help()
on python objects
"""

dozen = 12  # int
dozen = 12.3  # float
dozen = None  # NoneType
dozen = True  # bool
print(f"{type(dozen) =}")
print(f"{id(dozen)  =}")
print(f"{dozen      =}")

print(f"{dir(dozen) =}")

help(dozen)


print("=" * 40)
mountain = "Himalayas"  # string
print(f"{type(mountain) =}")
print(f"{id(mountain)   =}")
print(f"{mountain       =}")

print(f"{dir(mountain) =}")

help(mountain)
help(str)
help(mountain.isalpha)

# NOTE: help() usage differs only for string objects
