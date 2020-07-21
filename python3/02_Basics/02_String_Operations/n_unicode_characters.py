#!/usr/bin/python
"""
Purpose: unicode characters

ASCII - english characters & commonly used symbols
      - 0 to 127

      65 - A
      66 - B 
      67 - C
      .....
      97 - a
      98 - b 
      99 - c
"""
# chr() & ord()

print(f"{ord('A') =}") # 65
print(f"{ord('B') =}") # 66
print(f"{ord('C') =}") # 67
print()

print(f"{ord('a') =}") # 97
print(f"{ord('b') =}") # 98
print(f"{ord('c') =}") # 99
print()

print(f"{ord('1') =}") # 49
print(f"{ord('2') =}") # 50
print(f"{ord('3') =}") # 51
print()

print(f"{ord('$') =}") # 36
print(f'{chr(36)  =}') # '$'

# print(f"{ord('ap') =}") # 36
# TypeError: ord() expected a character, but string of length 2 found

print(f'{chr(0)    =}') # '\x00'
print(f'{chr(127)  =}') # '\x7f'

# > 127 ---> unicode characters
print(f'{chr(129)  =}')  # '\x81'

print('\u20B9')  # \uXXX - unicode character
print('\u018e')
print(u'noe\u0308l')
print()

print('\046')
print('\x24')   # \x... - hexadecimal number 
print('\xf1')


# One-character Unicode strings can also be created with the chr() built-in function
print(chr(57344))  # '\ue000'
print(ord('\ue000'))  # 57344

for i in range(300):
      print(i, chr(i))

print('chr(127)     :', chr(127))
print(f'{chr(127) =}')

for i in range(3000, 3500):
      print(i, chr(i))


# https://home.unicode.org/
