#!/usr/bin/python3
"""
Purpose: Raising exceptions
"""

# raise
# RuntimeError: No active exception to reraise

# raise Exception()
# Exception

# raise Exception('This is an error')
# Exception: This is an error

# raise ValueError()
# ValueError

# raise TypeError()

# raise NameError('This is name error')
# NameError: This is name error

try:
    num1 = int(input("Enter an integer:"))
    num2 = int(input("Enter an integer:"))
    if num2 == 0:
        # raise Exception("Ensure that num2 is NON-ZERO")
        raise ZeroDivisionError("Ensure that num2 is NON-ZERO")
except ZeroDivisionError as ze:
    print(repr(ze))
except Exception as ex:
    print(repr(ex))
else:
    division = num1 / num2
    print(f"{division =}")
