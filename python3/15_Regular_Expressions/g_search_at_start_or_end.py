"""
Purpose: Regular Expressions

Question: How to make re.search() to work like re.match ?

pattern
    ^   To make to check at the start of string
    $   To make to check at the end of string
"""

import re

result = re.search("pyTHon", "Programming is good in PYThon", re.I)
print(f"\nresult:{result}")

# TO Enforce to search at the end
result = re.search("pyTHon$", "Programming is good in PYThon", re.I)
print(f"\nresult:{result}")

result = re.search("pyTHon$", "Programming in python is gqqewd", re.I)
print(f"\nresult:{result}")

# TO Enforce to search at the start
result = re.search("^pyTHon", "Programming is good in PYThon", re.I)
print(f"\nresult:{result}")

result = re.match("pyTHon", "Programming is good in PYThon", re.I)
print(f"\nresult:{result}")

result = re.search("^pyTHon", "PYThon Programming is good", re.I)
print(f"\nresult:{result}")

result = re.match("pyTHon", "PYThon Programming is good", re.I)
print(f"\nresult:{result}")

if result:
    print(f"result.group():{result.group()}")
    print(f"result.span() :{result.span()}")
    print(f"result.start():{result.start()}")
    print(f"result.end()  :{result.end()}")
