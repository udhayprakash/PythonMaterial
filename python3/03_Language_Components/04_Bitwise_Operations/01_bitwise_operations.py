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

#                           128  64  32 16 8 4 2 1
num1 = 60            # 60 = 0     0   1  1 1 1 0 0 
num2 = 13            # 13 = 0     0   0  0 1 1 0 1 
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

num3 =  num1           # -61 = 1100 0011
print("Line 4 - Value of num3 is ",num3) 

num3 = num1 << 2       # 240 = 1111 0000
print("Line 5 - Value of num3 is ",num3) 

num3 = num1 >> 2       # 15 = 0000 1111
print("Line 6 - Value of num3 is ",num3) 


# NOTE:
# A left shift by n bits is equivalent to multiplication by pow(2, n) without overflow check.
# A right shift by n bits is equivalent to division by pow(2, n) without overflow check.