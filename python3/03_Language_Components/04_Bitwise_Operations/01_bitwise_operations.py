#!/usr/bin/python
"""
Purpose: bitwise operations 

&   binary AND
|   binary OR
^   binary XOR
~   binary 1's complement
<<  binary Left Shift 
>>  binary right shift 
"""

#                      128   64  32 16 8 4 2 1
num1 = 60       # 60 =  0     0   1  1 1 1 0 0 
num2 = 13       # 13 =  0     0   0  0 1 1 0 1 
                # ----------------------------
                #     & 0     0   0  0 1 1 0 0
                #     | 0     0   1  1 1 1 0 1
                #     ^ 0     0   1  1 0 0 0 1

num3 = num1 & num2        # 12 = 0000 1100
print("Line 1 - Value of num3 is ",num3) 

num3 = num1 | num2        # 61 = 0011 1101 
print("Line 2 - Value of num3 is ",num3) 

num3 = num1 ^ num2        # 49 = 0011 0001
print("Line 3 - Value of num3 is ",num3) 

num3 = ~ num1           # -61 = 1100 0011
print("Line 4 - Value of num3 is ",num3) 

num3 = num1 << 2       # 240 = 1111 0000
print("Line 5 - Value of num3 is ",num3) 

num3 = num1 >> 2       # 15 = 0000 1111
print("Line 6 - Value of num3 is ",num3) 


#             128 64 32 16   8 4 2 1
# 12 -          0  0  0  0   1 1 0 0
# <<2           0  0  1  1   0 0 0 0  =  48
#                          


# NOTE:
# A left shift by n bits is equivalent to multiplication by pow(2, n) without overflow check.
# A right shift by n bits is equivalent to division by pow(2, n) without overflow check.


print('-----------------------------------------------')
print('bitwise Operations')
# >> <<
myNewNumber = 4
print('myNewNumber =', myNewNumber)

myNewNumber <<= 1  # myNewNumber = myNewNumber << 1
print('myNewNumber = ', myNewNumber)
#     8 4 2 1
# 4   0 1 0 0  = 0 * 8 + 1 * 4 + 0 * 2 + 0 * 1  = 4
# <<  1 0 0 0  = 1 * 8 + 0 * 4 + 0 * 2 + 0 * 1  = 8

# 13  1 1 0 1
#  7  0 1 1 1
# 15  1 1 1 1

result = 14 >> 2
print("14 >> 2 = ", result)
#        8 4 2 1
# 14     1 1 1 0
# >>1    0 1 1 1  = 0 * 8 + 1 * 4 + 1 * 2 + 1 * 1 = 7
# >>2    0 0 1 1  = 0 * 8 + 0 * 4 + 1 * 2 + 1 * 1 = 3

# result = 3 << 2
# print("3 << 2 = ", result)
#        8 4 2 1
# 3      0 0 1 1
# <<2    1 1 0 0  =>  12


calculated_result = 10 << 4
print('10 << 4', calculated_result)
#            128    64    32    16    8   4   2   1
# 10                                  1   0   1   0
# 20                             1    0   1   0          1st shift
# 40                       1     0    1   0              2nd shift
# 80                 1     0     1    0                  3rd shift
# 160        1       0     1     0                       4th shift
