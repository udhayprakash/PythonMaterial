#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

print '  python Production  '
print
print '  python Production  '.strip()
print '  python Production  '.strip('p')
print '  python Production  '.strip('p ')
print '  python Production  '.strip('p thno')
print '  python Production  '.strip('p thnoy')
print
print '  python Production  '.strip()
print '  python Production  '.lstrip()
print '  python Production  '.rstrip()

print ' abcba '.lstrip('a ')
print ' abcba '.rstrip('a ')
print
# HOw to covert a string to a list
print 'Python Production'.split(' ')
print 'Python Production'.split('r')
print 'Python Production'.split('t')

print 'Python Production'.split('p')
print 'Python Production'.split('P')
print 'Python Production'.rsplit('P')
print 'Python Production'.split('Prod')
print
# HOw to convert list of strings to a single string
print ''.join(['Python', 'Production', 'language'])
print '@'.join(['Python', 'Production', 'language'])
print '___'.join(['Python', 'Production', 'language'])
print
print '___'.join('Python Production'.split('P'))
print 'P'.join('Python Production'.split('P'))
print 'R'.join('Python Production'.split('P'))
print ' '.join('Python Production'.split(' '))

print '--------STRING FORMATTING-------'
print '' % ()
print '%d' % (12)
# print '%d'%('12')  # TypeError: %d format: a number is required, not str
print '%s' % ('12')
print '%f' % (12.34)
print '%f' % (12)
# %d - integer
# %s - string/char
# %f - floating-point

print 'lucky number is %d only.' % (786)
print 'lucky number is %d only.' % 786
print 'pi value is %f!!!!!!!!!!' % (3.1416)
print 'my name is %s - %s.' % ('Udhay', 'Prakash')

print 'My name is %s. I am %d old paying a tax of %f'
print 'My name is %s. I am %d old paying a tax of %f' % ('Udhay', 33, 15.5)
print 'My name is %r. I am %r old paying a tax of %r' % ('Udhay', 33, 15.5)
# print 'My name is %s. I am %d old paying a tax of %f'%('Udhay', 33 )
  #TypeError: not enough arguments for format string
