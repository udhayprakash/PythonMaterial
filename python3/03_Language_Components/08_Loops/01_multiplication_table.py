#!/usr/bin/python
"""
initialization
while loop- condition
    logic
    increment/decrement
"""
# NOTE: i++, i--, --i, ++i (unary operations) are not supported in python

i = 0
while i < 10:
    i += 1
    j = 0
    while j <10:
        j+=1
        # print(i, '*', j, '=', i *j )
        # print('%2d * %2d = %3d'%(i, j, i*j))
        # print('{:2} * {:2} = {:3}'.format(i, j, i *j))
        # print(f'{i:2} * {j:2} = {i*j:3}')
        print(f'{str(i).zfill(2)} * {str(j).zfill(2)} = {str(i*j).zfill(3)}')
    print('-'* 10)

#  Assignment 
#  Display the multiplication table horizontally 
