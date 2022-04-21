#!/usr/bin/python3
"""
Purpose: Exception handling

In [8]: int('123')
Out[8]: 123

In [9]: int('123.123')
-----------------------------------------------------------ValueError                Traceback (most recent call last)<ipython-input-9-262f8b9ed82e> in <module>
----> 1 int('123.123')

ValueError: invalid literal for int() with base 10: '123.123'

In [10]: float('123.123')
Out[10]: 123.123

In [11]: float('123')
Out[11]: 123.0

In [1]: eval('123')
Out[1]: 123

In [2]: eval('123.1323')
Out[2]: 123.1323

In [3]: eval('None')

In [4]: eval('True')
Out[4]: True

In [5]: eval('123 + 100')
Out[5]: 223

In [6]: name = 'sometihing'

In [7]: eval('name')
Out[7]: 'sometihing'
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
