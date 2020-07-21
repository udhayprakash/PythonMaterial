#!/usr/bin/python
"""
Purpose: assertions

    Useful in unit testing 
    Validates the given condition

SYNTAX: 
    assert <condition>, "<exception message if condition is incorrect>"
"""

assert 12 + 10 == 22
assert 12 + 10 == 22, "Wrong answer"
# assert 12 + 10 != 22, "Wrong answer"  # AssertionError: Wrong answer

try: 
    assert 12 + 10 != 22, "Wrong answer"
except AssertionError as ex:
    print(str(ex))

