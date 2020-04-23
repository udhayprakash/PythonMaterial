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

    choice = eval(input("Choose your option: "))
    if choice == 1:
        add1 = eval(input("Add this: "))
        add2 = eval(input("to this: "))
        print(f'{add1} + {add2} = {add1 + add2}')
    elif choice == 2:
        sub2 = eval(input("Subtract this: "))
        sub1 = eval(input("from this: "))
        print(f'{sub1} - {sub2} = {sub1 - sub2}')
    elif choice == 3:
        mul1 = eval(input("Multiply this: "))
        mul2 = eval(input("with this: "))
        print(f'{mul1} * {mul2} = {mul1 * mul2}')
    elif choice == 4:
        div1 = eval(input("Divide this: "))
        div2 = eval(input("by this: "))
        print(f'{div1} / {div2} = {div1 / div2}')
    elif choice == 5:
        break

print("Thank you for using calculator!")
