#!/usr/bin/python
"""
Purpose: closure example demo
"""


def outer(num1):
    num3 = 30
    def wrapper(num2):
        result = num1 + num2 + num3
        return result

    print('wrapper.func_closure', wrapper.__closure__)
    return wrapper

outer_result = outer(10)

print('outer_result', outer_result)
print('outer_result()', outer_result(20))

# print num3

# print dir(outer)
print('outer.func_closure', outer.__closure__)
