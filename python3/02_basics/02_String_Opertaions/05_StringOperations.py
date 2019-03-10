#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

print('  python Production  ')
print()
print('  python Production  '.strip())
print('  python Production  '.strip('p'))
print('  python Production  '.strip('p '))
print('  python Production  '.strip('p thno'))
print('  python Production  '.strip('p thnoy'))  # 'Producti'
print()
print('  python Production  '.strip())
print('  python Production  '.lstrip())
print('  python Production  '.rstrip())
print('  python Production  '.lstrip('p thnoy'))
print('  python Production  '.rstrip('p thnoy'))

print(' abcba '.lstrip('a '))
print(' abcba '.rstrip('a '))
print()
# How to convert a string to a list
print('Python Production'.split(' '))
print('Python Production'.split('r'))
print('Python Production'.split('t'))

print('Python Production'.split('p'))
print('Python Production'.split('P'))
print('Python Production'.split('n'))
print('Python Production'.rsplit('P'))
print('Python Production'.split('Prod'))
# print 'Python Production'.split('') # ValueError: empty separator
print(''.split(' ')) 
print()
# How to convert a string to a list
print(list('Python Production'))

print() 
# HOw to convert list of strings to a single string
print(''.join(['Python', 'Production', 'language']))
print('@'.join(['Python', 'Production', 'language']))
print('___'.join(['Python', 'Production', 'language']))

print()
print('___'.join('Python Production'.split('P')))
print('P'.join('Python Production'.split('P')))
print('R'.join('Python Production'.split('P')))
print(' '.join('Python Production'.split(' ')))

print('Python Production'.replace('P', 'R'))
