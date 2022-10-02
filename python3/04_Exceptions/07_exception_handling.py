#!/usr/bin/python3
"""
Purpose: Exception handling

In [1]: int("123")
Out[1]: 123

In [2]: int("123.123")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In [2], line 1
----> 1 int("123.123")

ValueError: invalid literal for int() with base 10: '123.123'

In [3]: float("123.123")
Out[3]: 123.123

In [4]: float("123")
Out[4]: 123.0

In [5]: eval("123")
Out[5]: 123

In [6]: eval("123.123")
Out[6]: 123.123

In [7]: eval("None")

In [8]: eval("True")
Out[8]: True

In [9]: eval("123 + 100")
Out[9]: 223

In [10]: name = "something"

In [11]: eval(name)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In [11], line 1
----> 1 eval(name)

File <string>:1

NameError: name 'something' is not defined

In [12]: eval("name")
Out[12]: 'something'

"""
try:
    num1 = eval(input("Enter an integer:"))
    num2 = eval(input("Enter an integer:"))
    division = num1 / num2
# except ValueError as ve:
#     # print(f'{ve =}')
#     print('Please enter integers only')
except ZeroDivisionError as ze:
    print(f"{ze =}")
    print("Denominator cant be zero")
except TypeError as te:
    print(f"te = {te}")
except Exception as ex:
    print(f"Unhandled Error: {repr(ex)}")
else:
    print(f"{division = }")

# NOTE: Though we handle with specific exception based on seen errors,
# It is always recommended to have absolute(umbrella) exception to
# handle any unknown runtime errors.

# NOTE: exception handling should be defined from lower to higher hierarchy.
