#!/usr/bin/python

"""
Purpose: Demonstration of Arithmetic Operations


Integer family
	int
	long  - python 2 only 
	float

	complex
	bool
"""

# + - * / // %
# NOTE: PEP 8 recommends to place one space around the operator

num1 = 10  # int
num2 = 200  # int

print("num1=", num1)
print('num2=', num2)

print('-----------------------------')
print("Arithmetic Operations")
print('-----------------------------')

print('Addition')
print('num1 + num2 = ', num1 + num2)
print()
print('Subtraction')
print('num1 - num2 = ', num1 - num2)
print()
print('Multiplication')
print('num1 * num2 = ', num1 * num2)
print()
print('Division')
print('num1 / num2 = ', num1 / num2)

# print()
# # integers - int, long, float
# print('type(num1)= ', type(num1))
# print('type(num2)= ', type(num2))

# int + int  = int
# int / int  = int

# int < long < float

# int + long = long
# int + float = float
# long + float = float


num3 = 3445678909876545678909876556789098765
# the max. integer that can be computed depends on the capability of the machine

print('num3 = ', num3)
print('type(num3)= ', type(num3))

print('num1 + num3= ', num1 + num3)  # int + long = long



print('num1', num1)  # int
num4 = 3.15
print('num4', num4)  # float

result = num1 + num4 # int + float = float
print('result', result, type(result))

# going back to division

# print('10/2= ', 10 / 2)  # int/int = int
# print('10/5= ', 10 / 5)  # int/int = int

# print('10/3= ', 10 / 3)  # int/int = int         # 3
# print('10/3.0= ', 10 / 3.0)  # int/float = float     # 3.333333

# print()
# # type conversions
# # int()
# # float()
# # long()

# print('int(3.333333)=', int(3.333333))
# print('float(3) = ', float(3))
# print('float(3.333) = ', float(3.333))

# print()
# print('10/3= ', 10 / 3)
# print('10/float(3)= ', 10 / float(3))

# print()
# print(num1/num2/10)
# print('num1 / num2 = ', num1 / num2)  # int/int
# print('float(num1) / num2 = ', float(num1) / num2)
# print('float(num1 / num2) = ', float(num1 / num2))  # wrong

# print()
print('floor division  //')
print('10//2', 10 // 2)
print('10//5', 10 // 5)

# print('10/3 = ', 10 / 3)
# print('10//3 = ', 10 // 3)  # 3 < 3.3333 < 4
# print()
# print('10/3.0 = ', 10 / 3.0)
# print('10//3.0 = ', 10 // 3.0)  # 3 < 3.3333 < 4
# print('-10//3.0 = ', -10 // 3.0)  # -4 < -3.3333 <  -3
# .0

# print('10/2.5 = ', 10 / 2.5)
# print('10//2.5 = ', 10 // 2.5)  # 4.0

'''
>>> 13/2
6
>>> 13/2.0
6.5
>>> 13//2.0  # 6 < 6.5 < 7
6.0
>>> - 13//2.0 # -7 < -6.5 < -6
-7.0
>>> - 13/2.0  # true result
-6.5
>>> # -7 < -6.5 < -6
'''
