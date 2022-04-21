#!/usr/bin/python
"""
Purpose: unit testing using asserts

Symantic:
    assert <statement>, "Error Message, if statement is incorrect"
"""

assert 1 + 2 == 3
assert 1 + 2 == 3, "1+2 is not equal to 3"

try:
    assert 10 - 34 > 3
except AssertionError as ex:
    print(f"Error is {ex}")


try:
    assert 10 - 34 > 3, "This statement is incorrect"
except AssertionError as ex:
    print(f"Error is {ex}")


assert 1 == True
# assert '1' == str(True)
