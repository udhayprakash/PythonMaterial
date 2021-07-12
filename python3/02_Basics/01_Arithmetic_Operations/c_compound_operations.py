#!/usr/bin/python3
"""
Purpose: compound operations
"""
num = 100 + 324
print('num =', num)  # 424

num = 100
print('num =', num)  # 100

num = num + 10
print('num =', num)  # 110

# NOTE: In cases, where the same variable is present both the sides,
# then compound operations are valid

num += 10            # num = num + 10
print('num =', num)  # 120

num -= 20            # num = num - 20
print('num =', num)  # 100

num *= 1.5           # num = num * 1.5
print('num =', num)  # 150.0

num *= (1.5 + 20 - 4/5)  #num = num *(1.5 + 20 - 4/5)
print('num =', num)  # 3105.0

other_num = 50
num /= other_num     # num = num / other_num
print('num =', num)  # 62.1

num %= 10            # num = num % 10
print('num =', num)  # 2.1000000000000014

num **= 10           # num = num ** 10
print('num =', num)  # 1667.9880978201113

# NOTE: python doesn't support unary operations ;
# ++i, i++, --i, i--
# it should used as i += 1, i -=1
