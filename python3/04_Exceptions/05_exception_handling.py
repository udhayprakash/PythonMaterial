#!/usr/bin/python
"""
Purpose: Exception Handling 
"""
try: 
    num1 = int(input('Enter an integer:'))
    num2 = int(input('Enter an integer:'))
except Exception as ex:
    print(f'{ex =}')
    print('Please enter integers only')
else:
    try:
        division = num1 / num2 
    except Exception as ex1:
        print(f'{ex1 =}')
        print('Denominator cant be zero')
    else:
        print(f'{division = }')

# NOTE: In this problem context, 
# finally is not needed
