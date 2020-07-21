#!/usr/bin/python
"""
Purpose: Exception Handling

NOTE: Syntax errors cant be handled by except

"""

# import builtins
# print(dir(builtins))
# print(f'{__builtins__ =')


num1 = 10     

#  num2 = 200    # IndentationError: unexpected indent

# for i in range(10):
# print(i)       # IndentationError: expected an indented block

# 10/0    # ZeroDivisionError: division by zero
# 10 % 0  # ZeroDivisionError: integer division or modulo by zero
# 10 // 0 # ZeroDivisionError: integer division or modulo by zero

# Method 1
try:
    10 / 0
except:
    pass 

# Method 2
try:
    # 10 // 0               # ZeroDivisionError
    # 10 / 0                # ZeroDivisionError
    # 10 % 0                # ZeroDivisionError
    # 10 + 0               
    # 10 + '0'              # TypeError
    # 10 + None             # TypeError
    # int('3.1415')         # ValueError

    name = 1232
    name.upper()            # AttributeError
except Exception as ex:
    print('ex      :', ex)
    print('str(ex) :', str(ex))
    
    print('repr(ex):', repr(ex))
    print(f'{ex = }')


print('\nnext statement')