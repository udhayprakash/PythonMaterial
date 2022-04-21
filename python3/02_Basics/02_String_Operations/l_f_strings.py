#!/usr/bin/python3
"""
Purpose: String formatting using F-strings
        Introducted in python 3.6
"""
print('' % ())           # OLD Style
print('{}'.format(''))   # NEW Style
print(f'{""}')           # F-String
print()

print('Hello {name}')
print('Hello {name}'.format(name='world'))
name = 'World'
print(f'Hello {name}')
# print(f"Hello {name1}")
# NameError: name 'name1' is not defined
print()

number = 12312.123
print(f'number is {number}')

# python operations on data within the f-string
print(f'Hello {name.upper()}')
print(f'Hello {name.title()}')
print(f'number is {int(number)}')
value = 123123
print(f'The value is {float(value) + 3}')
print()

value = 1234567890.88
print(f'{value}')   # 1234567890.88
print(f'{value:}')  # 1234567890.88
print(f'{value:,}') # 1,234,567,890.88
print(f'{value:_}') # 1_234_567_890.88
print(f'{value:-}') # 1234567890.88
print(f'{value:+}') # +1234567890.88
print()

print(f'{"left aligned":<20}')  # 'left aligned        '
print(f'{"right aligned":>20}') # '       right aligned'
print(f'{"centered":^20}')      # '      centered      '
print(f'{"centered":-^20}')      # '      centered      '
print()

print(f'{1024}', 1024)         # 1024 1024
print(f'{1024:d}', 1024)       # 1024 1024
print(f'{1024:b}', bin(1024))  # 10000000000 0b1000000000
print(f'{1024:o}', oct(1024))  # 2000 0o2000
print(f'{1024:x}', hex(1024))  # 400 0x400
print(f'{1024:X}', hex(1024))  # 400 0X400
print()

import math

print('math.pi', math.pi)    # 3.141592653589793
print(f'{math.pi}')          # 3.141592653589793
# print(f'{math.pi:d}')
print(f'{math.pi:f}')  # 3.141593
print(f'{math.pi:F}')  # 3.141593
print(f'{math.pi:g}')  # 3.14159

print()
print(f'{math.pi:f}')     # 3.141593
print(f'{math.pi:9f}')    #  3.141593
print(f'{math.pi:9.3f}')  #     3.142
print()

print(f"{'quoted string'}")
print(f'{"quoted string"}')

# To get braces in string
print(f'{4 * 10}')      # 40
print(f'{{4*10}}')      # {4*10}
print(f'{{{4 * 10}}}')  # {40}

print(f'{"quoted string"}')     # quoted string
print(f'{{"quoted string"}}')   # {"quoted string"}
print(f'{{{"quoted string"}}}') # {quoted string}

# Processing escape sequences
print(f'x={4 * 10}\n')
print(fr'x={4 * 10}\n')


# format specifier
import decimal

width = 10
precision = 4
value = decimal.Decimal('12.34567')
print(f'result: {value}')
print(f'result: {value:{width}.{precision}}')

# String concatenation
x = 10
y = 'hi'
print('a' 'b' f'{x}' '{c}' f'str<{y:^4}>' 'd' 'e')
# Each f-string is entirely evaluated before being concatenated to adjacent f-strings.
print()

# !s, !r, !a
name = 'Python:αλεπού'
# !s - str()
print(f'{name!s}')  # Python:αλεπού
# !r - repr()
print(f'{name!r}')  # 'Python:αλεπού'
# !a - ascii()
print(f'{name!a}')  # 'Python:\u03b1\u03bb\u03b5\u03c0\u03bf\u03cd'
print()

from datetime import datetime
today = datetime.now()
print(f'today:%Y-%m-%d') # '2021-07-20'
print()

#######################
# f-string vs str.format
d = {'a': 10, 'b': 20}
print('a={d[a]}'.format(d=d))
print(f'a={d["a"]}')

a = 'b'
print(f'a={d[a]}')

print('{i[";]}'.format(i={'";': 4}))

format(14, '#b'), format(14, 'b') # ('0b1110', '1110')
f'{14:#b}', f'{14:b}'             # ('0b1110', '1110')


# Ref: https://miguendes.me/73-examples-to-help-you-master-pythons-f-strings
