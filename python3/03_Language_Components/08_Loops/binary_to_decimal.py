#!/usr/bin/python
"""
Purpose:  binary to decimal
"""
jbinary = str(input('Enter a binary number i.e., in 0s and 1s:'))

sum1, p = 0, 1
for i in jbinary:
    sum1 += int(i) * 2 ** (len(jbinary) - p)
    p += 1
# print('Its decimal value is =',sum)
print("Decimal(%s)=%r" % (jbinary, sum1))
