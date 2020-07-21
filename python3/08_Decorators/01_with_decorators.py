#!/usr/bin/python
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


# # outer().inner()

# result = outer()
# print(result)
# result()

# outer()()

# -------------------------------
def add(a, b):
    return a + b


def div(n1, n2):
    return n1 / n2


# def outer(func):
#     def inner():
#         try:
#             result = ''
#             print(f'{func =}')
#         except Exception as ex:
#             return ex
#         else:
#             return result
#     return inner

# result_add = outer(add)()  # func =<function add at 0x000001FC5A66F820>
# result_div = outer(div)()   # func =<function div at 0x000001FC5A66F8B0>


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

print(f'{outer(add)(10, 20)     =}')  
result_add = outer(add)
print(f'{result_add(10, 20)     =}')
print(f'{result_add("10", "20") =}')
print(f'{result_add(10, "20")   =}')
print(f'{result_add("10", 20)   =}')

assert outer(add)(10, 20) == result_add(10, 20) == add(10, 20)

print()
print(f'{outer(div)(10, 20)     =}') 

result_div = outer(div)                 # reference  to inner
print(f'{result_div(10, 20)     =}')
print(f'{result_div(0, 20)      =}')
print(f'{result_div(10, 0)      =}')
