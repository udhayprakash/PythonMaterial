#!/usr/bin/python
"""
Purpose: timeit - with setup
"""
import timeit

print('\n-----with setup')
"""
with setup,
    #python -m timeit -s "lang = 'Python'; char = 't'"  "char in lang"
    1000000 loops, best of 5: 141 nsec per loop

    #python -m timeit -s "lang = 'Python'; char = 't'"  "lang.find(char)"
    500000 loops, best of 5: 626 nsec per loop

"""
print(timeit.timeit('char in lang', setup="lang = 'Python'; char = 't'"))
# 0.15269916100000014
print(timeit.timeit('lang.find(char)', setup="lang = 'Python'; char = 't'"))
# 0.4405657889999999

# The same can be done alternatively,
print('\n-----with setup, alternatively')
t = timeit.Timer('char in lang', setup="lang = 'Python'; char = 't'")
print(t.timeit())
print(t.repeat())

print('\n----when test code has multiple lines')
"""
#python -m timeit "try:" "  str.__bool__" "except AttributeError:" "  pass"
100000 loops, best of 5: 2.01 usec per loop

#python -m timeit "if hasattr(str, '__bool__'): pass"
200000 loops, best of 5: 1.38 usec per loop

#python -m timeit "try:" "  int.__bool__" "except AttributeError:" "  pass"
1000000 loops, best of 5: 200 nsec per loop

#python -m timeit "if hasattr(int, '__bool__'): pass"
1000000 loops, best of 5: 256 nsec per loop
"""
# attribute is missing
s = """\
try:
    str.__bool__
except AttributeError:
    pass
"""
print(timeit.timeit(stmt=s, number=100000))

s = "if hasattr(str, '__bool__'): pass"
print(timeit.timeit(stmt=s, number=100000))

# attribute is present
s = """\
try:
    int.__bool__
except AttributeError:
    pass
"""
print(timeit.timeit(stmt=s, number=100000))

s = "if hasattr(int, '__bool__'): pass"
print(timeit.timeit(stmt=s, number=100000))

print('\n-----passing globals to use global variables')


def f(x):
    return x ** 2


def g(x):
    return x ** 4


def h(x):
    return x ** 8


# print(timeit.timeit('[func(42) for func in (f,g,h)]'))
# NameError: name 'f' is not defined
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))

# from timeit import timeit


# print(timeit("factorial(999)", "from math import factorial", number=10))


# from math import factorial
# print(timeit(lambda: factorial(999), number=10))
