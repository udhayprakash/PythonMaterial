#!/usr/bin/python3
"""
Purpose: Exception Handling

    Exception Hierarchy
"""
# try:
#     num1 = int(input('Enter an integer:'))
#     num2 = int(input('Enter an integer:'))
#     division = num1 / num2
# except Exception as ex:
#     print(repr(ex))
# else:
#     print(f'{division = }')


# try:
#     num1 = int(input('Enter an integer:'))
#     num2 = int(input('Enter an integer:'))
#     division = num1 / num2
# except ValueError as ve:
#     print(f'{ve =}')
# else:
#     print(f'{division = }')


try:
    num1 = int(input('Enter an integer:'))
    num2 = int(input('Enter an integer:'))
    division = num1 / num2
except ValueError as ve:
    # print(f'{ve =}')
    print('Please enter integers only')
except ZeroDivisionError as ze:
    # print(f'{ze =}')
    print('Denominator(num2) cant be zero')
else:
    print(f'{division = }')
