#!/usr/bin/python
"""
Type converters:
    int(),  float(), 
    
    str(), repr()

    bin(), hex(), oct()
"""
#####################################
num1 = 12
print('num1      ', num1)
print('type(num1)', type(num1))

# int to int
num2 = int(num1)
print('num2      ', num2)
print('type(num2)', type(num2))

#####################################
num3 = 1233222222222222222999999993333333
print('num3      ', num3)
print('type(num3)', type(num3))

# long to int  --> no exception, but not converted
num4 = int(num3)
print('num3      ', num3)
print('type(num3)', type(num3))

#####################################
num3 = 1233222222222222222999999993333333
print('num3      ', num3)
print('type(num3)', type(num3))

# long to int  --> no exception, but not converted
num4 = int(num3)
print('num4      ', num4)
print('type(num4)', type(num4))

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
# print 'num8      ', num8
# print 'type(num8)', type(num8)

# ----------------
#     128 64 32 16 8 4 2 1
# 9 -> 0   0  0  0 1 0 0 1
# 23 >           1 0 1 1 1

# decimal to binary 
bin(9)

# 8 4 2 1
# 1 0 0 1
# binary to decimal 
print(int(bin(9), base=0))  # '0b1001'
print((9).bit_length())  # 4

print(int(bin(-9), base=0))  # '-0b1001'
print((-9).bit_length())  # 4

# decimal to hex : 0-9 A-F
hex(9)
# hex to decimal 
int(hex(9), base=16)

# decimal to oct :0-7
oct(9)
# oct to decimal 
int(oct(9), base=8)

#### Checks ##################
(-2.0).is_integer()  # True 
(3.2).is_integer()  # False
