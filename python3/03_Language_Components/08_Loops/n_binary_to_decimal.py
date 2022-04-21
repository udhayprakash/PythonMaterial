#!/usr/bin/python
"""
Purpose: Binary to Decimal conversion,
         without using builtin functions

            128  64 32 16 8 4 2 1
             0   0   0  0 1 1 1 1 => 15
             0   0   1  0 1 0 0 0 => 40
             1   0   1  0 1 0 0 1 => 169

"""

# binary_number = '10101001'
binary_number = '11100010101001'

# Method 1
decimal_number = int(binary_number, base=2)
print(binary_number, decimal_number)


# Method 2

sum_value = 0
for loop_index, each_digit in enumerate(binary_number[::-1]):
    if each_digit == '1':
        # print(loop_index, pow(2 , loop_index))
        sum_value += pow(2, loop_index)

print(f'{sum_value =}')
