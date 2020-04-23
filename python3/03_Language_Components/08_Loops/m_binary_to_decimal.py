#!/usr/bin/python
"""
Purpose: Binary to Decimal conversion, without using builtin functions

128  64 32 16 8 4 2 1
1     0  1  0 1 0 0 1


"""


binary_number = '10101001'

# Method 1
print(int(binary_number, base=2))

# Method 2
bin_num_length = len(binary_number)
sum_value = 0
for loop_index, each_digit in enumerate(binary_number[::-1]):
    sum_value += int(each_digit) * pow(2, loop_index)

print(sum_value)
