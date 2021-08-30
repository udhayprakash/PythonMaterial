#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with two arguments and two return values
"""
#- UNPACKING ------------------------------
num1 = 123
num2 = 323
print(f'num1:{num1} num2:{num2}')

num1, num2 = 123, 323   # unpacking
print(f'num1:{num1} num2:{num2}')

print()
num1 = 123
num2 = 323
num3 = 423
print(f'num1:{num1} num2:{num2} num3:{num3}')

num1, num2, num3 = 123, 323, 423  # unpacking
print(f'num1:{num1} num2:{num2} num3:{num3}')

print()
# num1, num2, num3 = 123, 323  #ValueError: not enough values to unpack (expected 3, got 2)
# num1, num2 = 123, 323, 423  # ValueError: too many values to unpack (expected 2)

num1 = 123, 323, 423  # treats as a tuple
print(f'{type(num1), num1}')
print()

print(f'{int(1123.123) =}') # returns single value
print(f'{pow(2, 3)     =}') # returns single value
print(f'{divmod(20, 3) =}') # returns two values

num = int(1123.123)
powVal = pow(2, 3)
quotient, remainder = divmod(20, 3)


# Function Definition
def hello():
    return 123, 45

# Function Call
hello()

result = hello()
print(f'{type(result)}, {result}')   # <class 'tuple'>, (123, 45)

result1 = result[0]
result2 = result[1]
print(f'result1: {result1}')   # 123
print(f'result2: {result2}')   # 45
print()
#-----------------------------------

result1, result2 = hello()    # unpacking
print(f'result1: {result1}')  # 123
print(f'result2: {result2}')  # 45
