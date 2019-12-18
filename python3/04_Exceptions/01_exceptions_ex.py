#!/usr/bin/python
"""
Purpose: Exception Handling

Syntax errors cant be handled by except
"""

 # num1 = 10  # IndentationError: unexpected indent

# # print(10 / 0)
# try:
#     result = 10 / 0
# except:
#     print('Cant divide by zero')


# if result:
# print(result)  # IndentationError: expected an indented block

#   print('Hello') # IndentationError: unindent does not match any outer indentation level

# ----------------------------------------
try:
    result = 10 / 10
    # result = 10 / 0
    result = '10' / 0
except Exception as ex:
    # print(f'ex          : {ex}')
    # print(f'str(ex)     : {str(ex)}')
    print(f'repr(ex)    : {repr(ex)}')
else:
    print('code in try block executed without errors')
finally:
    print('finally closing it')

print('out side statement')
# work flow
# when no error     : try -> else   -> finally
# when error occured: try -> except -> finally

# else and finally blocks are optional

