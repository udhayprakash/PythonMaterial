#!/usr/bin/python3
"""
Purpose: Raising exceptions
"""
# raise
# RuntimeError: No active exception to reraise

# raise Exception()
# raise Exception('This is an Error')  # Exception: This is an Error

# raise ValueError()

# raise TypeError()
# raise NameError('This is name error')


try:
    num1 = int(input('Enter an integer:'))
    num2 = int(input('Enter an integer:'))
    if num2 == 0:
        raise ZeroDivisionError('ENsure that num2 is non-zero')
except Exception as ex:
    print(ex)
else:
    division = num1 /num2
    print(f'{division =}')

