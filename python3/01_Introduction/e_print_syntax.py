#!/usr/bin/python
"""
Purpose: print() function - syntax and usage - continuation

Escape sequences
    \t - tab space
    \n - new line

    r'' - raw string

"""
print('hello world python')
print('hello \tworld \tpython')
print('hello \tworld \npython')

print('hello \tworld \\npython')
print(r'hello \tworld \npython') # to not consider escape sequences

print()
# --------------------
# print(data, sep=' ', end = '\n')

print('hello') # default end='\n'
print('world')

print('hello', end='\n')
print('world', end='\n')

print('hello', end='___')
print('world')  # default end='\n'

print('hello', end='\t')
print('world')  # default end='\n'

print('hello', 'python', 12132, end='\t') # default sep= ' '
print('world')  # default end='\n'

print('hello', 'python', 12132, end='\t', sep=';')
print('world')  # default end='\n'


print(1, 2, 3, 4, 5, sep=';', end='\t')
print('a', 'b', 'c', 'd', sep='-') # default end='\n'


# ----------------------
print()
print('#$%*&^(*;')
print('He\bi')  # \b - overwrites previous character
print('12\b34')

print('\u20B9')  # \uXXX - unicode character
print('\u018e')

print('\046')
print('\x24')   # \x... - hexadecimal number 
print('\xf1')
