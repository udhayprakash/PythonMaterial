#!/usr/bin/python3
"""
Purpose: Bitwise Operations

    &   binary AND    -> If all are 1, result is 1
    |   binary OR     -> If all are 0, only then result is 0
    ^   binary XOR    -> If total count of 1's are odd, it results in 1, else 0
    ~   binary 1's complement
    <<  binary Left Shift
    >>  binary right shift

     126 64 32 16  8 4  2  1
60 -   0  0  1  1  1 1  0  0
13 -   0  0  0  0  1 1  0  1
----------------------------
&  -   0  0  0  0  1 1  0  0 = (8 * 1 + 4 * 1) = 12
|  -   0  0  1  1  1 1  0  1 = (32 + 16 + 8 + 4 + 1) = 61
^  -   0  0  1  1  0 0  0  1 = (32 + 16 + 1) = 49
"""
num1 = 60
num2 = 13

print('num1=', num1, bin(num1))  # 0b111100
print('num2=', num2, bin(num2))  # 0b1101

num3 = num1 & num2  # 12 = 0000 1100
print("Line 1 - Value of num3 is ", num3)


num3 = num1 | num2  # 61 = 0011 1101
print("Line 2 - Value of num3 is ", num3)

num3 = num1 ^ num2  # 49 = 0011 0001
print("Line 3 - Value of num3 is ", num3)

num3 = ~ num1  # -61 = 1100 0011
print("Line 4 - Value of num3 is ", num3)

num3 = num1 << 2  # 240 = 1111 0000
print("Line 5 - Value of num3 is ", num3)

num3 = num1 >> 2  # 15 = 0000 1111
print("Line 6 - Value of num3 is ", num3)

print('10 << 1 =', 10 << 1)
print('10 << 2 =', 10 << 2)
print('10 << 3 =', 10 << 3)
print('10 << 4 =', 10 << 4)
#            128    64    32    16    8   4   2   1
# 10                                  1   0   1   0
# 20                             1    0   1   0          1st shift
# 40                       1     0    1   0              2nd shift
# 80                 1     0     1    0                  3rd shift
# 160        1       0     1     0                       4th shift

print()
print('160 >> 1 =', 160 >> 1)  # 80
print('160 >> 2 =', 160 >> 2)  # 40
print('160 >> 3 =', 160 >> 3)  # 20
print('160 >> 4 =', 160 >> 4)  # 10

# NOTE:
# A left shift by n bits is equivalent to multiplication by pow(2, n) without overflow check.
# A right shift by n bits is equivalent to division by pow(2, n) without overflow check.

