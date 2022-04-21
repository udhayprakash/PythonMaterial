#!/usr/bin/python3
"""
Purpose: Data Type Conversions

        int - decimal       - int() -base 10  (0-9)
            - binary        - bin() -base  2  (0-1)
            - hexadecimal   - hex()
            - octal         - oct()
        float
            float()
        String
            str()


int -> float
int -> str

float -> int
float -> str

str  -> int
str -> float
"""
num = 12
print('num=', num, type(num))

# int -> float
print(12, float(12))  # 12 12.0

# int -> str
print(12, str(12))   # 12 '12'

# float -> int
print(3.1416, int(3.1416))  # 3.1416,  3
print(3.1416, str(3.1416))  # 3.1416, '3.1416'

# str  -> int
print('23', int('23'))      # '23 ', 23
print('23 ', int('23 '))    # '23 ', 23
# print('2 3', int('2 3'))  # ValueError: invalid literal for int() with base 10: '2 3'
# print('two', int('two'))  # ValueError: invalid literal for int() with base 10: 't

# print('23.24', int('23.24')) # ValueError: invalid literal for int() with base 10: '23.24'

# str -> float
print('23   ', float('23'))    # '23   ', 23.0
print('23.24', float('23.24'))  # '23.24', 23.24
print('23.  ', float('23.'))   # '23.  ', 23.0
# print('2 3. ', float('2 3.'))  # ValueError: could not convert string to float: '2 3.'

float()              # 0.0
float('+1.23')       # 1.23
float('   -12345\n')  # -12345.0
float('1e-003')      # 0.001
float('+1E6')        # 1000000.0
float('-Infinity')   # -inf

# NOTE: Anything can be converted to str; but not vice versa
print('str(12)', str(12))
print('str(121233.12323)', str(121233.12323))
print('str(-0.000012)', str(-0.000012))
print('str(True)', str(True))
print('str(None)', str(None))
print()

# int Value is same in all four representations
# decimal, binary, hexadecimal & octal

num1 = 33
print('num1 =', num1, type(num1))  # -> Decimal form

# decimal -> binary form
print(23, bin(23), type(bin(23)))  # 23, '0b10111'
# print(23.24, bin(23.24), type(bin(23.24))) # TypeError: 'float' object cannot be interpreted as an integer
print(23.24, bin(int(23.24)))     # 23.24, '0b10111'

#       128 64 32 16  8 4 2 1
# 23 ->   0  0  0  1  0 1 1 1  = 16  + 4 + 2 + 1 = 23
#  9 ->   0  0  0  0  1 0 0 1

print('bin(9)', bin(9))    # '0b1001'

# binary -> decimal form
print('0b1001', int('0b1001', base=0))  # 9
print('1001  ', int('1001', base=0))   # 1001
print('bin(9)', int(bin(9), base=0))   # 9

print((9).bit_length())  # 4 <- '0b1001'
print((23).bit_length())  # 5 <- '0b10111'

# Octal -> 0-7
# decimal -> octal
print('oct(9)  ', oct(9))   # '0o11'
print('oct(-23)', oct(-23))  # '-0o27'

'%#o' % 10, '%o' % 10               # ('0o12', '12')
format(10, '#o'), format(10, 'o')   # ('0o12', '12')
f'{10:#o}', f'{10:o}'               # ('0o12', '12')

# octal -> decimal
print(int(oct(9), base=8))   # 9
print(int('0o11', base=8))   # 9
print(int('11', base=8))     # 9
print(int('11'))             # 11

# Hexadecimal - 0-9 A-F
# decimal -> hexadecimal
print('hex(9)  ', hex(9))    # '0x9'
print('hex(-23)', hex(-23))  # '-0x17'

# hexadecimal -> decimal
print(int(hex(-23), base=16))  # -23
print(int('-0x17', base=16))  # -23
print(int('-17', base=16))    # -23
print(int('-17'))             # -17

'%#x' % 255, '%x' % 255, '%X' % 255  # ('0xff', 'ff', 'FF')
format(255, '#x'), format(255, 'x'), format(255, 'X')  # ('0xff', 'ff', 'FF')
f'{255:#x}', f'{255:x}', f'{255:X}'  # ('0xff', 'ff', 'FF')


# Checks ##################
# is_integer -> Return True if the float is an integer.
print((-2.0).is_integer())  # True
print((-2.1).is_integer())  # False
print((-1.9999).is_integer())  # False
print()

# ---- roman numbers
print(int('42'))  # 42
print(int('४२'))  # 42
print(int('٤٢'))  # 42
print(int('४२', 16))  # 66
print(int('४२', base=16))  # 66

# Telugu numbers
for num in ['౦', '౧', '౨', '౩', '౪', '౫', '౬', '౭', '౮', '౯']:
    print(num, int(num, base=16))

# Ref: https://unicode-table.com/
