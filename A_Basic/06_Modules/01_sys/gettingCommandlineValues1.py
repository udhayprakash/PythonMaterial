#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: Demo of Command line inputs
"""

import sys

# for i in  dir(sys):
#     print i
#
#
# print '-' * 80
#
# # Run time value
# word = raw_input('Enter some word:')
#
# print 'You entered:'+ word
#

# sys.argv

print "sys.argv     :", sys.argv
print "len(sys.argv):", len(sys.argv)

winningTicket = '123Alpha'

if len(sys.argv) >= 2:
    userEnteredTicket = sys.argv[1]
else:
    print 'Please enter the ticket number\n'
    print 'USAGE:'
    print '      python gettingCommandlineValues.py 231asdas'
    print '__file__ :', __file__
    print '      python', __file__, '231sads'
    sys.exit(1)

if winningTicket == userEnteredTicket:
    print 'You won the lottery'
else:
    print 'Try again!'
