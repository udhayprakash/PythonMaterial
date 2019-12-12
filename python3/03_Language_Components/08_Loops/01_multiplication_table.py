#!/usr/bin/python
"""
initialization
while loop- condition
    logic
    increment/decrement
"""
# NOTE: i++, i--, --i, ++i (unary operations) are not supported in python

print('\nincrementing loop with increment first')
i = 0
while i < 10:
    i = i + 1
    print(i, end=' ')

print('\n\nincrementing loop with increment last')
i = 0
while i < 10:
    print(i, end=' ')
    i = i + 1

print('\n\nincrementing loop with increment last')
i = 0
while i <= 10:
    print(i, end=' ')
    i = i + 1

print('\n\ndecrementing loop with decrement first')
j = 10
while j > 0:
    j = j - 1
    print(j, end=' ')

print('\n\ndecrementing loop with decrement last')
j = 10
while j > 0:
    print(j, end=' ')
    j = j - 1




###########################################
print('\n\n Multiplication Table')
first = 0
while first < 10:
    first += 1
    # print(first)

    second = 0
    while second < 10:
        second += 1
        # print(first, '*', second, '=', first * second)
        # print(str(first) + ' * ' + str(second) + ' = ' + str(first * second))
        # print('%2d * %2d = %3d' % (first, second, first * second))
        # print('{0:2} * {1:2} = {2:3}'.format(first, second, first * second))
        print(f'{first:2} * {second:2} = {first * second:3}')
    print('-' * 12)


'''
Assignment
-----------
1) WAP to display the multiplication table from 10 to 1, for the first 10 tables
10 * 10 = 100
10 *  9 =  90
10 *  8 =  80
10 *  7 =  70
10 *  6 =  60
10 *  5 =  50
10 *  4 =  40
10 *  3 =  30
10 *  2 =  20
10 *  1 =  10

2) Assignment - Display the multiplication table horizontally 

01 * 01 = 001 | 02 * 01 = 002 | 03 * 01 = 003 | 04 * 01 = 004 | 05 * 01 = 005 | 06 * 01 = 006 | 07 * 01 = 007 | 08 * 01 = 008 | 09 * 01 = 009 | 10 * 01 = 010
01 * 02 = 002 | 02 * 02 = 004 | 03 * 02 = 006 | 04 * 02 = 008 | 05 * 02 = 010 | 06 * 02 = 012 | 07 * 02 = 014 | 08 * 02 = 016 | 09 * 02 = 018 | 10 * 02 = 020
01 * 03 = 003 | 02 * 03 = 006 | 03 * 03 = 009 | 04 * 03 = 012 | 05 * 03 = 015 | 06 * 03 = 018 | 07 * 03 = 021 | 08 * 03 = 024 | 09 * 03 = 027 | 10 * 03 = 030
01 * 04 = 004 | 02 * 04 = 008 | 03 * 04 = 012 | 04 * 04 = 016 | 05 * 04 = 020 | 06 * 04 = 024 | 07 * 04 = 028 | 08 * 04 = 032 | 09 * 04 = 036 | 10 * 04 = 040
01 * 05 = 005 | 02 * 05 = 010 | 03 * 05 = 015 | 04 * 05 = 020 | 05 * 05 = 025 | 06 * 05 = 030 | 07 * 05 = 035 | 08 * 05 = 040 | 09 * 05 = 045 | 10 * 05 = 050
01 * 06 = 006 | 02 * 06 = 012 | 03 * 06 = 018 | 04 * 06 = 024 | 05 * 06 = 030 | 06 * 06 = 036 | 07 * 06 = 042 | 08 * 06 = 048 | 09 * 06 = 054 | 10 * 06 = 060
01 * 07 = 007 | 02 * 07 = 014 | 03 * 07 = 021 | 04 * 07 = 028 | 05 * 07 = 035 | 06 * 07 = 042 | 07 * 07 = 049 | 08 * 07 = 056 | 09 * 07 = 063 | 10 * 07 = 070
01 * 08 = 008 | 02 * 08 = 016 | 03 * 08 = 024 | 04 * 08 = 032 | 05 * 08 = 040 | 06 * 08 = 048 | 07 * 08 = 056 | 08 * 08 = 064 | 09 * 08 = 072 | 10 * 08 = 080
01 * 09 = 009 | 02 * 09 = 018 | 03 * 09 = 027 | 04 * 09 = 036 | 05 * 09 = 045 | 06 * 09 = 054 | 07 * 09 = 063 | 08 * 09 = 072 | 09 * 09 = 081 | 10 * 09 = 090
01 * 10 = 010 | 02 * 10 = 020 | 03 * 10 = 030 | 04 * 10 = 040 | 05 * 10 = 050 | 06 * 10 = 060 | 07 * 10 = 070 | 08 * 10 = 080 | 09 * 10 = 090 | 10 * 10 = 100

HINTS: string formatting, str.zfill(), while/for loop
'''