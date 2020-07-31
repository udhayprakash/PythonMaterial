#!/usr/bin/python3
"""
Purpose: Exception Handling

NOTE: Syntax errors cant be handled by except

"""
# import builtins
# print(dir(builtins))

num1 = 10
#  num2 = 20  # IndentationError: unexpected indent

# for i in range(5):
# print(i)    # IndentationError: expected an indented block

# 10 / 0  # ZeroDivisionError: division by zero
# 10 % 0  # ZeroDivisionError: integer division or modulo by zero
# 10 // 0   # ZeroDivisionError: integer division or modulo by zero

# num3 = int(input('Enter num:'))
# print(num3)

# # Method 1
# try:
#     10 / num3
# except:
#     pass

# # Method 2
# try:
#     10 / num3
# except Exception as ex:
#     print('ex      :', ex)
#     print('str(ex) :', str(ex))

#     print('repr(ex):', repr(ex))
#     print(f'{ex = }')


# Method 2 - example 2
try:
    # 10 // 0               # ZeroDivisionError
    # 10 / 0                # ZeroDivisionError
    # 10 % 0                # ZeroDivisionError
    10 + 0
    # 10 + '0'              # TypeError
    # 10 + '0'              # TypeError
    # 10 + None             # TypeError

    float('3.1415')
    # int('3.1415')         # ValueError

    name = 12123
    name.upper()            # AttributeError
except Exception as ex:
    print('ex      :', ex)
    print('str(ex) :', str(ex))

    print('repr(ex):', repr(ex))
    print(f'{ex = }')


print('\nnext statement')
