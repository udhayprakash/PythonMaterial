#!/usr/bin/python3
"""
Purpose: Creating Exception Handling Decorator
    - writing generic decorator with variable args & keyword args handling
"""


def exception_handling(func):  # -> Decorator function
    def inner(*args, **kwargs):  # v1, v2
        try:
            result = func(*args, **kwargs)
            # print(f'{func =}')
        except Exception as ex:
            return ex
        else:
            return result

    return inner


def div(n1, n2):  # 2 arguments
    return n1 / n2


result = exception_handling(div)
print(result(4, 2))
print(result(4, 0))
print()


# ----


def add(n1, n2, n3):  # 3 arguments
    return n1 + n2 + n3


result_add = exception_handling(add)
print(result_add(10, 20, 30))

print(result_add(10, 20, "30"))
print(result_add(10, 20))
