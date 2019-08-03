#!/usr/bin/python
"""
Purpose: String formatting
        OLD STYLE string formatting
%d - integer
%i - integer

%c - single char
%s - string/char

%f - floating-point
%F - floating-point

%o - octal 
%x - hexadecimal lowercase 
%X - hexadecimal uppercase
"""

print('' % ())
print('%d' % (12))
print('%i' % (12))
# print('%d'%('12'))  # TypeError: %d format: a number is required, not str

print()
print('%s' % ('12'))
print('%f' % (12.34))
print('%f' % (12))
print('%s' % (True))

print()
#%o - octal 
print('%o' % (12), oct(12))
#%x - hexadecimal lowercase 
print('%x' % (12), hex(12))
#%X - hexadecimal uppercase 
print('%X' % (12), hex(12))

print('%s' % ('12'))
print('%c' % ('1'))

print()
print('%f' % (12.34)) # 12.340000
print('%F' % (12.34)) # 12.340000

print()
print('%g' % (12.34)) # 12.34
print('%G' % (12.34)) # 12.34

print()
print('%e' % (12.34)) # 12.34
print('%E' % (12.34)) # 12.34

print()
import math 
print('pi', math.pi)     # 3.141592653589793
print('%d'% math.pi)     # 3
print('%f'% math.pi)     # 3.141593
print('%9f'% math.pi)    #  3.141593
print('%9.3f'% math.pi)  #     3.142
###########################################################
print()
print('lucky number is %d only.' % (786))
print('lucky number is %d only.' % 786)
print('pi value is %f!!!!!!!!!!' % (3.1416))
print('my name is %s - %s.' % ('Udhay', 'Prakash'))

print()
print('My name is %s. I am %d old paying a tax of %f')
print('My name is %s. I am %d old paying a tax of %f' % ('Udhay', 99, 15.5))
print('My name is %r. I am %r old paying a tax of %r' % ('Udhay', 78, 15.5))
# print('My name is %s. I am %d old paying a tax of %f'%('Udhay', 33 ))
#TypeError: not enough arguments for format string

print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
