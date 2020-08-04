#!/usr/bin/python
"""
Purpose: Exception Handling 
    Handling Multiple Exceptions together
"""
try:
    num1 = eval(input('Enter an integer:'))
    num2 = eval(input('Enter an integer:'))
    division = num1 / num2
except (ValueError, ZeroDivisionError, TypeError) as ex1:
    print(f'{ex1 =}')
except Exception as ex:
    print(f'Unhandled Error: {repr(ex)}')
else:
    print(f'{division = }')
