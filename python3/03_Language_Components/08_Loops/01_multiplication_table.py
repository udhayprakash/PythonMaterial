#!/usr/bin/python
"""
initialization
while loop- condition
    logic
    increment/decrement
"""
# NOTE: i++, i--, --i, ++i (unary operations) are supported in python
num1 = 0 
while num1 < 10:
    num1 += 1
    # if num1 == 3:
    #     break
    num2 = 0
    while num2 < 10:
        num2 += 1
        # print(num1, '*', num2, '=', num1 * num2)
        # print('%2d * %2d = %2d'%(num1, num2, num1 * num2))
        # print('{0:2d} * {1:2d} = {2:2d}'.format(num1, num2, num1 * num2))
        print(f'{num1} * {num2} = {num1 * num2}')
    print('-'*10) # string repetition operation
else:
    print('All loops executed')

print('Next statement')





















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

