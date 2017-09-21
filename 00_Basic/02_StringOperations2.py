#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

language = 'Python Programming'
print 'language       = ', language
print 'type(language) = ', type(language)

junkData = '$%^%^&^* &^\'*&^ * uhk'
print 'junkData       = ', junkData
print 'type(junkData) = ', type(junkData)
print
print 'STRING OPERATIONS'
print '--------------------------------------'
print 'string Indexing'

#P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
#0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing
#-18                                    -3 -2 -1 - reverse indexing
#

print len(language)
print 'language[0] :', language[0]
print 'language[14]:', language[14]
print 'language[6] :', language[6]
print 'language[17] :', language[17]
#print 'language[18] :', language[18] # IndexError:

print
print 'language[-0] :', language[-0]
print 'language[-3] :', language[-3]

print 'language[-18] :', language[-18]
#print 'language[-19] :', language[-19] # # IndexError

print '------------------------------'
print 'String Slicing'
#P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
#0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing
#-18                                    -3 -2 -1 - reverse indexing
#
print language
print language[0:11]
print language[5:17]
print language[7:10]
# In python, it doesn't include the last value
print language[0:5]
print language[0:6]

print language[7:18]
print language[7:999]  # 999 index isn't present
print language[45:87]  # indexes are not present
# striing slicing - string[start_index, final_index, step]
# Default - step = +1

print language[7:18]
print language[7:18:1]
print language[7:18:-1]  # 7-1 = 6 ; it is not between 7 and 18

print language[18:7:-1] # 18-1 = 17
print language[18:7:-3] # 18-3 = 15

# default start_index = 0
# default final_index = last index of string
print 'language[:7] :', language[:7]  # equal to language[0:7]
print 'language[0:] :', language[0:]
print 'language[6:] :', language[6:]

print 'language[:]  :', language[:]
print language

print 'language[::] :', language[::]  # default step = +1
print 'language[::-1] :', language[::-1]  # string reversal
# If step is -ve, then start_index = last string index and
# final_index = 0

print '==========================================='
print 'String Attributes'
print 'language      :', language
print 'type(language):', type(language)
print 'dir(language) :', dir(language)

print language
print 'language.capitalize():', language.capitalize()
print 'language.title()     :', language.title()
print 'language.upper()     :', language.upper()
print 'language.lower()     :', language.lower()
print 'language.swapcase()  :', language.swapcase()

print 'language.isupper()   :', language.isupper()
print 'language.islower()   :', language.islower()
print 'language.istitle()   :', language.istitle()


print 'language.find("t")   :', language.find('t')
print 'language.find("n")   :', language.find('n')
print 'language.rfind("n")   :', language.rfind('n')

print 'language.find("Prog")   :', language.find('Prog')

print 'language.index("t")   :', language.index('t')
print 'language.index("n")   :', language.index('n')
print 'language.rindex("n")   :', language.rindex('n')

print 'language.index("Prog")   :', language.index('Prog')

# index vs find
print 'language.find("Q")   :', language.find('Q')
#print 'language.index("Q")   :', language.index('Q')  # ValueError
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

print '--------STRINg FORMATTING-------'
print ''%()
print '%d'%(12)
# %d - integer
# %s - string/char
# %f - floating-point
print 'lucky number is %d only.'%(786)
print 'pi value is %f!!!!!!!!!!'%(3.1416)
print 'my name is %s.'%('Udhay Prakash')

print 'My name is %s. I am %d old paying a tax of %f'
print 'My name is %s. I am %d old paying a tax of %f'%('Udhay', 33, 15.5 )
