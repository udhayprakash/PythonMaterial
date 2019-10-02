#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def div(a, b):
    return a / b


def outer(func):
    def inner(*args, **kwargs):  # (a, b):
        # print(f'In inner(), func:{func}') 
        try:
            func(*args, **kwargs)  # (a, b)          # div(), add()
        except Exception as ex:
            return repr(ex)
        else:
            return func(*args, **kwargs)  # (a, b)   # div(), add()

    return inner


result = outer(div)
print(result(4, 2))
print(result(4, 0))
print()


def add(n1, n2, n3):
    return n1 + n2 + n3


temp_var = outer(add)  # refence  to inner
print(temp_var(2, 3, 4))
print(temp_var('a', 3, 4))
