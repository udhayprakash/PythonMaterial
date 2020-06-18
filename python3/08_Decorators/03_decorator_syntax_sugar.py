#!/usr/bin/python
"""
Purpose: Decorator Syntax Sugar 
"""

def expection_handling(func):              # -> Decorator function
    def inner(*args, **kwargs):  # v1, v2
        try:
            result = func(*args, **kwargs)
            # print(f'{func =}')
        except Exception as ex:
            return ex
        else:
            return result
    return inner


def div(n1, n2):             # 2 arguments
    return n1 / n2


result = expection_handling(div)
print(result(4, 2))
print(result(4, 0))
print()


@expection_handling
def div1(n1, n2):             # 2 arguments
    return n1 / n2

print(div1(4, 2))
print(div1(4, 0))
print()

# ------------------------------------
def add(n1, n2, n3):         # 3 arguments
    return n1 + n2 + n3


result_add = expection_handling(add)
# print(result_add(10, 20))    # add() missing 1 required positional argument: 'n3'
print(result_add(10, 20, 30))
print(result_add(10, 20, '30'))
print()

@expection_handling
def add1(n1, n2, n3):         # 3 arguments
    return n1 + n2 + n3


print(add1(10, 20, 30))
print(add1(10, 20, '30'))
