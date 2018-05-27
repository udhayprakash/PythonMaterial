#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

language = 'Python Programming'
print 'language       = ', language
print 'type(language) = ', type(language)

print '==========================================='
print 'String Attributes'
print 'language      :', language
print 'type(language):', type(language)
print 'dir(language) :', dir(language)

# string concatenation 
mystr1 = 'Taj'
mystr2 = "Mahal"
result = mystr1 + mystr2
print 'result=', result 

result = mystr1.__add__(mystr2)
print 'result=', result 

print language
print 'language.capitalize():', language.capitalize()
print 'language.title()     :', language.title()
print 'language.upper()     :', language.upper()
print 'language.lower()     :', language.lower()
print 'language.swapcase()  :', language.swapcase()

print 'language.isupper()   :', language.isupper()
print 'language.islower()   :', language.islower()
print 'language.istitle()   :', language.istitle()
print 'language.isdigit()   :', language.isdigit()
print 'language.isalpha()   :', language.isalpha()
print 'language.isalnum()   :', language.isalnum()
print 'language.isspace()   :', language.isspace()


print 'language.find("t")   :', language.find('t')
print 'language.find("n")   :', language.find('n')
print 'language.rfind("n")   :', language.rfind('n')

print 'language.find("Prog")   :', language.find('Prog')
print 'language.rfind("Prog")  :', language.rfind('Prog')

print 'language.index("t")   :', language.index('t')
print 'language.index("n")   :', language.index('n')
print 'language.rindex("n")  :', language.rindex('n')

print 'language.index("Prog")   :', language.index('Prog')
print 'language.rindex("Prog")   :', language.rindex('Prog')

# index vs find
print 'language.find("Q")   :', language.find('Q')
# print 'language.index("Q")   :', language.index('Q')  # ValueError
print
print '  python Production  '
print '  python Production  '.strip()
print '  python Production  '.strip('p')
print '  python Production  '.strip('p ')
print '  python Production  '.strip('p thno')

print '  python Production  '.strip()
print '  python Production  '.lstrip()
print '  python Production  '.rstrip()


print ' abcba '.lstrip('a ')
print ' abcba '.rstrip('a ')

print 'Python Production'.split(' ')
print 'Python Production'.split('r')
print 'Python Production'.split('p')
print 'Python Production'.split('P')
print 'Python Production'.rsplit('P')


print ''.join(['Python', 'Production'])
print '@'.join(['Python', 'Production'])
print '___'.join(['Python', 'Production'])
print '___'.join('Python Production'.split('P'))
print 'P'.join('Python Production'.split('P'))
print ' '.join('Python Production'.split(' '))


print '--------STRING FORMATTING-------'
print ''%()
print '%d'%(12)
# print '%d'%('12')  # TypeError: %d format: a number is required, not str
print '%s'%('12')
print '%f'%(12.34)
print '%f'%(12)
# %d - integer
# %s - string/char
# %f - floating-point
print 'lucky number is %d only.'%(786)
print 'lucky number is %d only.'% 786
print 'pi value is %f!!!!!!!!!!'%(3.1416)
print 'my name is %s.'%('Udhay Prakash')

print 'My name is %s. I am %d old paying a tax of %f'
print 'My name is %s. I am %d old paying a tax of %f'%('Udhay', 33, 15.5 )
# print 'My name is %s. I am %d old paying a tax of %f'%('Udhay', 33 ) 
#   #TypeError: not enough arguments for format string
