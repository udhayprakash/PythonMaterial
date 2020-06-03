#!/usr/bin/python
"""
Purpose: Exception Handling 

In [1]: eval('123')
Out[1]: 123

In [2]: eval('12312.123')
Out[2]: 12312.123

In [3]: eval('None')

In [4]: print(eval('None'))
None

In [5]: eval('True')
Out[5]: True

In [8]: name = 'someting'

In [9]: eval('name')
Out[9]: 'someting'
"""
try: 
    num1 = eval(input('Enter an integer:'))
    num2 = eval(input('Enter an integer:'))
    division = num1 / num2 
except ValueError as ve:
    # print(f'{ve =}')
    print('Please enter integers only')
except ZeroDivisionError as ze:
    # print(f'{ve =}')
    print('Denominator cant be zero')
except TypeError as te:
    print(f'te = {te}')
except Exception as ex:
    print(f'Unhandled Error: {ex}')
else:
    print(f'{division = }')

# NOTE: Though we handle with specific exception based on seen errors, 
# It is always recommended to have absolute(unmbrella) exception to 
# handle any unknown runtime errors. 

# NOTE: exception handling should be defined from lower to higher heirarchy.
