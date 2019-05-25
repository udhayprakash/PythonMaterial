#!/usr/bin/python
"""
Purpose: String formatting
        OLD STYLE string formatting
"""

print('' % ())
print('%d' % (12))
# print '%d'%('12')  # TypeError: %d format: a number is required, not str

print()
print('%s' % ('12'))
print('%f' % (12.34))
print('%f' % (12))
print('%s' % (True))
# %d - integer
# %s - string/char
# %f - floating-point

print()
print('lucky number is %d only.' % (786))
print('lucky number is %d only.' % 786)
print('pi value is %f!!!!!!!!!!' % (3.1416))
print('my name is %s - %s.' % ('Udhay', 'Prakash'))

print()
print('My name is %s. I am %d old paying a tax of %f')
print('My name is %s. I am %d old paying a tax of %f' % ('Udhay', 99, 15.5))
print('My name is %r. I am %r old paying a tax of %r' % ('Udhay', 78, 15.5))
# print 'My name is %s. I am %d old paying a tax of %f'%('Udhay', 33 )
#TypeError: not enough arguments for format string