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
print 'len(language):', len(language)
print 'dir(language) :', dir(language)

# string concatenation
mystr1 = 'Taj'
mystr2 = 'Mahal'

result = mystr1 + mystr2
print 'result=', result

result = mystr1.__add__(mystr2)
print 'result=', result
print

print language
print 'language.capitalize():', language.capitalize()
print 'language.title()     :', language.title()
print 'language.upper()     :', language.upper()
print 'language.lower()     :', language.lower()
print 'language.swapcase()  :', language.swapcase()
print
print 'language.isupper()   :', language.isupper()
print 'language.islower()   :', language.islower()
print 'language.istitle()   :', language.istitle()
print 'language.isdigit()   :', language.isdigit()
print 'language.isalpha()   :', language.isalpha()
print 'language.isalnum()   :', language.isalnum()
print 'language.isspace()   :', language.isspace()
print

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing


print 'language.find("t")    :', language.find('t')
print 'language.find("n")    :', language.find('n')
print 'language.rfind("n")   :', language.rfind('n')
print
print 'language.find("Prog")   :', language.find('Prog')
print 'language.rfind("Prog")  :', language.rfind('Prog')
print
print 'language.index("t")       :', language.index('t')
print 'language.index("n")       :', language.index('n')
print 'language.rindex("n")      :', language.rindex('n')
print
print 'language.index("Prog")    :', language.index('Prog')
print 'language.rindex("Prog")   :', language.rindex('Prog')

# index vs find
print 'language.find("Q")   :', language.find('Q')
# print 'language.index("Q")   :', language.index('Q')  # ValueError
