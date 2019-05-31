#!/usr/bin/python
"""
initialization
while loop- condition
    logic
    increment/decrement
"""
# NOTE: i++, i--, --i, ++i (unary operations) are not supported in python

MIN = 1
MAX= 10

num1 = MIN
while num1 <= MAX:
    num2 = MIN
    while num2 <= MAX:
        # print(num1, '*',  num2, '=', num1 * num2)
        # print('%d * %d = %d'%(num1, num2, num1 * num2))
        # print('%2d * %2d = %3d'%(num1, num2, num1 * num2))
        # print('{:2} * {:2} = {:3}'.format(num1, num2, num1 * num2))
        print(f'{num1:2} * {num2:2} = {num1 * num2:3}')
        # num2 = num2 + 1
        num2 += 1

    print('-'* 15)
    # print(num1)
    # num1 = num1 + 1
    num1 += 1


# Assignment : display table hoizontally 
