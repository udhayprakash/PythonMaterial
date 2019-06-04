#!/usr/bin/python
"""
initialization
while loop- condition
    logic
    increment/decrement
"""
# NOTE: i++, i--, --i, ++i (unary operations) are not supported in python

num1 = 1
while num1 <= 10:
    num2 = 1 
    while num2 <= 10:
        # print(num1, '*', num2, '=', num1 * num2)
        # print(str(num1).zfill(2), '*', str(num2).zfill(2), '=',  str(num1 * num2).zfill(3))       
        # print('{:2} * {:2} = {:3}'.format(num1, num2, num1 * num2))
        print(f'{num1:2} * {num2:2} = {num1 * num2:3}')
        num2 += 1

    # num1 = num1 + 1
    num1 += 1
    print('-'* 15)


#  Assignment 
#  Display the multiplication table horizontally 
