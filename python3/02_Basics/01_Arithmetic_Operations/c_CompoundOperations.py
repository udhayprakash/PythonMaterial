#!/usr/bin/python
"""
Purpose: Component operations
    component operators
        += Adding and assigning
        -= Subtracting and assigning
        *= Multiply and assigning
        /= Divide and assigning
        //= floor division and assigning
        %=  remainder operation and assigning
        **= power operation and assigning
"""
num = 100
print('num =', num)  # 100

num = num + 20
print('num =', num)  # 120

# NOTE: In cases, where the same variable is present both the sides,
# then compound operations are valid

num += 20  # num = num + 20
print('num =', num)  # 140

num -= 3  # num = num - 3
print('num =', num)  # 137

num *= 1.5  # num = num * 1.5
print('num =', num)  # 205.5

num *= 1.5 + 20 - 4 / 5  # num = num * 1.5 + 20 - 4/5
print('num =', num)  # 4253.849999999999

other_num = 50
num /= other_num  # num = num / other_num
print('num =', num)  # 85.07699999999998

num %= 10
print('num =', num)  # 5.076999999999984

num **= 10
print('num =', num)  # 11378149.455105506

# python doesn't support unary operations ;
# ++i, i++, --i, i--
# it should used as i += 1, i -=1
