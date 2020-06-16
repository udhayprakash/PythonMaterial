#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with two arguments and two return values
"""

print(f'{pow(2, 3)     =}') # returns single value
print(f'{divmod(20, 3) =}') # returns two values

# Function Definition
def hello():
    return 123, 45


# Function Call
hello()

result = hello()
print(f'{type(result)}, {result}')

print()
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


######################################
print()
# Function Definition
def hello():
    return 123, 45


# Function Call
result = hello()
print(f'{type(result)}, {result}')   # <class 'tuple'>, (123, 45)

result1 = result[0]
result2 = result[1]
print(f'result1: {result1}')   # 123
print(f'result2: {result2}')   # 45
print()

result1, result2 = hello()    # unpacking
print(f'result1: {result1}')  # 123
print(f'result2: {result2}')  # 45
