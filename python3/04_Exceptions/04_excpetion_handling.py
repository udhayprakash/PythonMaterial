#!/usr/bin/python3
"""
Purpose: Additon operation, with exception handling
"""
# num1= 1000
# num2 = 2121

try:
    num1 = int(input('Enter an integer:'))
    num2 = int(input('Enter an integer:'))
except Exception as ex:
    print(f'Error is {ex=}')
else:
    result = num1 + num2
    print(result)
finally:
    print('------------------------')

# NOTE: In this problem context,
# finally is not needed