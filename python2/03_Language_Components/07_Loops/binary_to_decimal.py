#!/usr/bin/env python

#binary to decimal
jbinary=str(input('Enter a binary number i.e., in 0s and 1s:'))

sum1,p=0,1
for i in binary:
    sum1+=int(i)*2**(len(binary)-p)
    p+=1
#print('Its decimal value is =',sum)
print('Decimal(%s)=%r' %(binary,sum))
