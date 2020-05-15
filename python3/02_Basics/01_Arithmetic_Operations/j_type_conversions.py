#!/usr/bin/python
"""
Basic Types: int, float, str
    int - decimal       - int()
        - binary        - bin()
        - hexadecimal   - hex()
        - octal         - oct()

Type converters:
    int(),  float(), 
    
    str(), repr()

    bin(), hex(), oct()
"""
#####################################
num1 = 12
print('num1      ', num1)
print('type(num1)', type(num1))

# int to int = int
num2 = int(num1)
print('num2      ', num2)
print('type(num2)', type(num2))

#####################################
num3 = 1233222222222222222999999993333333
print('num3      ', num3)
print('type(num3)', type(num3))

# int to int  --> no exception, but not converted
num4 = int(num3)
print('num3      ', num3)
print('type(num3)', type(num3))

#####################################
num5 = 3.14161718
print('num5      ', num5)
print('type(num5)', type(num5))

# float to int  --> decimal part will be truncated
num6 = int(num5)
print('num6      ', num6)
print('type(num6)', type(num6))

# number as string to int
num7 = int('356')
print('num7      ', num7)
print('type(num7)', type(num7))

# # string to int
# num8 = int('three') # ValueError: invalid literal for int() with base 10: 'Hello'
# print('num8      ', num8)
# print('type(num8)', type(num8))

# ----------------
#     128 64 32 16 8 4 2 1
# 9 -> 0   0  0  0 1 0 0 1
# 23 >           1 0 1 1 1

# decimal to binary
print('bin(9) ', bin(9))
print('bin(23)', bin(23))

# binary to decimal
print(int('0b1001', base=0))
print(int(bin(9), base=0))

print((9).bit_length())  # 4
print((23).bit_length())  # 5

print(int(bin(-9), base=0))  # '-0b1001'
print((-9).bit_length())  # 4

# decimal to hex : A-F 0-9
print('hex(9)', hex(9))
# hex to decimal
int(hex(9), base=16)

# decimal to oct :0-7
print('oct(9)', oct(9))
# oct to decimal
int(oct(9), base=8)

# Checks ##################
print((-2.0).is_integer())  # True
print((3.2).is_integer())  # False
