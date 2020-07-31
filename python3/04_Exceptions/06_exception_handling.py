#!/usr/bin/python
"""
Purpose: Exception Handling 

    Exception Hierarchy
"""
try:
    num1 = int(input('Enter an integer:'))
    num2 = int(input('Enter an integer:'))
    division = num1 / num2
except ValueError as ve:
    # print(f'{ve =}')
    print('Please enter integers only')
except ZeroDivisionError as ze:
    # print(f'{ve =}')
    print('Denominator cant be zero')
else:
    print(f'{division = }')
