#!/usr/bin/python
"""
Purpose: String formatting using F-strings
"""

print('' % ())
print('{}'.format(''))
print(f'{""}')

print("Hello {name}")
print("Hello {name}".format(name='world'))
name = 'World'
print(f"Hello {name}")
# print(f"Hello {name1}")
# NameError: name 'name1' is not defined

# python operations on data within the f-string
print(f"Hello {name.upper()}")
print(f"Hello {name.title()}")

value = 123123
print(f'The value is {float(value) + 3}')

NAME = 'udhay'
AGE = 99
SALARY = 9999.9999
print(f'''
        Name  :{NAME} , Name  :{NAME}
        Age   :{AGE}
        Salary:{SALARY}''')

print()
value2 = 1234567890.88
print(f"{value}")  # 1234567890.88
print(f"{value:,}")  # 1,234,567,890.88
print(f"{value:_}")  # 1_234_567_890.88
print()

# To get quotes in string
# print(f'{\'quoted string\'}')  # SyntaxError
print(f"{'quoted string'}")
print(f'{"quoted string"}')

# To get braces in string
print(f'{4 * 10}')
print(f'{{4*10}}')
print(f'{{{4 * 10}}}')

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

# !s, !r, !a
name = 'Python:αλεπού'
# !s - str()
print(f'{name!s}')  # Python:αλεπού
# !r - repr()
print(f'{name!r}')  # 'Python:αλεπού'
# !a - ascii()
print(f'{name!a}')  # 'Python:\u03b1\u03bb\u03b5\u03c0\u03bf\u03cd'


#######################
# f-string vs str.format
d = {'a': 10, 'b': 20}
print('a={d[a]}'.format(d=d))
print(f'a={d["a"]}')

a = 'b'
print(f'a={d[a]}')

print('{i[";]}'.format(i={'";': 4}))
