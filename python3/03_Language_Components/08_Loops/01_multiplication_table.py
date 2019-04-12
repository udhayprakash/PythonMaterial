#!/usr/bin/python
"""
initialization
while loop- condition
    logic
    increment/decrement
"""
# NOTE: i++, i--, --i, ++i (unary operations) are supported in python

num1 = 1
while num1 <= 10: 
    num2 = 1
    while num2 <= 10: 
        print(f'{num1} * {num2} = {num1 * num2}')
        num2 = num2 + 1
    print('-'* 25)
    num1 = num1 + 1

















# MIN = 0
# MAX = 12

# a = MIN  # initialization
# while a < MAX:  # condition
#     a += 1  # increment
#     b = MIN
#     while b < MAX:
#         b += 1
#         # print a, '*', b, '=', a*b
#         # print "%d * %d = %d" % (a, b, a * b)
#         # print "%2d * %2d = %3d" % (a, b, a * b)
#         print("{0:2} * {1:2} = {2:3}".format(a, b, a*b))
#     print('-' * 18, a)
#     # break

