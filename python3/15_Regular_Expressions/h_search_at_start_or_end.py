#!/usr/bin/python3
"""
Purpose: Regular Expressions

Question: How to make re.search() to find at the end of string only

pattern
    ^   To make to check at the start of string
    $   To make to check at the end of string

    \A | Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.
    \Z | Matches the expression to its left at the absolute end of a string whether in single or multi-line mode.

"""
import re

# Method 1 - using ^ and $
result = re.search("abc$", "ABC123abcd", re.I)
print(f"\nresult:{result}")  # None

result = re.search("abc$", "ABC123abc", re.I)
print(f"\nresult:{result}")
if result:
    print(f"result.group():{result.group()}")  # abc

result = re.search("^abc", "ABC123abc", re.I)
print(f"\nresult:{result}")
if result:
    print(f"result.group():{result.group()}")  # ABC

# Method 2 - using \A and \Z
result = re.search("abc\Z", "ABC123abc", re.I)
print(f"\nresult:{result}")
if result:
    print(f"result.group():{result.group()}")  # abc

result = re.search("\Aabc", "ABC123abc", re.I)
print(f"\nresult:{result}")
if result:
    print(f"result.group():{result.group()}")  # ABC
