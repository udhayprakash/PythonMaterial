#!/usr/bin/python3
"""
Purpose: assertions

    Useful in unit testing
    Validates the given condition

SYNTAX:
    assert <condition>, "<exception message if condition is incorrect>"
"""
print(f"{10 + 2}")
print(f"{10 + 2 =}")
print(f"{10 + 2 == 12}")


if 10 + 2 == 12:
    print("This is True")
else:
    print("This is not correct")


assert 2 + 10 == 12, "Wrong answer"
assert 10 + 2 == 12, "Wrong answer"

# assert 12 + 10 == 12, "Wrong answer"
try:
    assert 12 + 10 == 12, "Wrong answer"
except AssertionError as ex:
    print(f"{ex =}")
