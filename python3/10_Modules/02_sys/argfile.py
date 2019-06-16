#!/usr/bin/python
"""
Purpose: Importance of sys.argv
"""
import sys
print('__file__', __file__)
print('len(sys.argv)', len(sys.argv))
print('sys.argv', sys.argv)

if len(sys.argv) != 2:
    print('PLease provide your lottery ticket no')
    print('USAGE:')
    print('      python argfile.py 231asdas')
    print('      python', __file__, '231sads')
    sys.exit(0)


print(sys.argv[1])
winning_ticket = '2312hj124'
user_ticket = sys.argv[1] #input('Enter ticket no:')  # '1231kjkjb'

if winning_ticket == user_ticket:
    print('You won the lottery')
else:
    print('Please try again!!!')
























# import time
# for i in range(90):
#     time.sleep(1)  # 1sec
# name = input('name=')
# print('Entered named is', name)


# import sys
#
# # print('__file__', __file__)
# # print('sys.argv', sys.argv, type(sys.argv))
#
# # if len(sys.argv) == 1:
# #     print('Enter properly')
# #     print(__file__, 'name')
# #     sys.exit(0)
#
# # name = sys.argv[1]
# # print('Entered name is', name)
#
#
# # sys.argv
#
# print("sys.argv     :", sys.argv)
# print("len(sys.argv):", len(sys.argv))
#
# winningTicket = '123Alpha'
#
# if len(sys.argv) == 1:

#
# userEnteredTicket = sys.argv[1]
#
# if winningTicket == userEnteredTicket:
#     print('You won the lottery')
# else:
#     print('You Lost. Try again!')
#
#
