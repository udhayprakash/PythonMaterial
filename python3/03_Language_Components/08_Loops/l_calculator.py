#!/usr/bin/python
"""
Purpose: Calculator

eval() - built-in function
    eval('10 ')
    Out[4]: 10
    eval('  10   ')
    Out[5]: 10
    eval('  10.34234   ')
    Out[6]: 10.34234

Output:
    1 
        Addition  
        12 3 23 45 23
        12+3+23+45+23

    1 
        Addition  
        12 3
        12+3
"""

while True:
    print('''
    ================================
    Welcome to calculator.py

    your options are:
        1) Addition
        2) Subtraction
        3) Multiplication
        4) Division

        5) Quit calculator.py
    ''')
    choice = input('Enter the choice:')
    if choice not in ('1', '2', '3', '4'):
        break
    
    space_sep_values = input('Enter values seperated by space:')
    # print(space_sep_values)
    # print(space_sep_values.split())
    if choice == '1':
        print('Addition Operation: ', end=' ')
        result = 0
        for each_val in space_sep_values.split():
            result += int(each_val)
    elif choice == '2':
        print('subtraction operation: ', end=' ')
        result = 0
        for each_val in space_sep_values.split():
            result -= int(each_val)
    elif choice == '3':
        print('Multiplication operation: ', end=' ')
        result = 1
        for each_val in space_sep_values.split():
            result *= int(each_val)
    elif choice == '4':
        print('Division operation: ', end=' ')
        result = 1
        for each_val in space_sep_values.split():
            result /= int(each_val)

    print(f'{result=}')

