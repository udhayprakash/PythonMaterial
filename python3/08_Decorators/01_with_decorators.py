#!/usr/bin/python3
"""
Purpose: Solving the problem with decorator function
"""


# def outer():
#     def inner():
#         try:
#             result = ''
#             print('TODO both add & div logic')
#         except Exception as ex:
#             return ex
#         else:
#             return result
#     return inner
#
#
# print(f'{outer() =}')  # outer.<locals>.inner
# print(f'{outer()() =}')  # ''
#
# result = outer()
# print(f'{result() =}')  # ''

# -======================================
def add(a, b):
    return a + b


def div(n1, n2):
    return n1 / n2


def outer(func):
    def inner():
        try:
            result = ''
            print(f'{func =}')
        except Exception as ex:
            return ex
        else:
            return result

    return inner


result_add = outer(add)()  # function add at 0x0000022E5425EA70>
print(f'{result_add =}')  # ''

result_div = outer(div)()  # <function div at 0x000001963F21EB00>
print(f'{result_add =}')  # ''
print()


# =================================
def outer(func):
    def inner(v1, v2):
        try:
            result = func(v1, v2)
            # print(f'{func =}')
        except Exception as ex:
            return ex
        else:
            return result

    return inner


print(f'{outer(add) =}')  # <function outer.<locals>.inner at 0x00000207FDB8EB90>

print(f'{outer(add)(10, 20)     =}')

result_add = outer(add)
print(f'{result_add(10, 20)     =}')
print(f'{result_add("10", "20") =}')
print(f'{result_add(10, "20")   =}')
print(f'{result_add("10", 20)   =}')

assert outer(add)(10, 20) == result_add(10, 20) == add(10, 20)

print()
print(f'{outer(div)(10, 20)     =}')

result_div = outer(div)  # reference  to inner
print(f'{result_div             =}')
print(f'{result_div(10, 20)     =}')
print(f'{result_div(0, 20)      =}')
print(f'{result_div(10, 0)      =}')
