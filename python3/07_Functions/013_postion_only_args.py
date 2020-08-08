#!/usr/bin/python3
"""
Purpose: Function with position-only arguments

    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        -----------    ----------     ----------
            |             |                  |
            |        Positional or keyword   |
            |                                - Keyword only
            -- Positional only

    When to use positional-only arguments
        Use positional-only if names do not matter or have no meaning, and there are only a few arguments which will always be passed in the same order.
        Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names.

NOTE: Introduced in python 3.8
"""
def multiply_then_add(a, b, c, d=10):
    return a + b + c + d

print(multiply_then_add(5, 10, 20))
print(multiply_then_add(5, 10, 20, 89))

print(multiply_then_add(5, 10, 20, d=89))
print(multiply_then_add(a=5, b=10, c=20, d=89))

# -------------------------------------
def multiply_then_add(a, b, c, /, d=10):
    return a + b + c + d

print(multiply_then_add(5, 10, 20, d=89))
# print(multiply_then_add(a=5, b=10, c=20, d=89))
# TypeError: multiply_then_add() got some positional-only arguments passed as keyword arguments: 'a, b, c'

# -----------------
print()
print(f'{pow(4, 2)       =}')
print(f'{pow(4, 2, 10)   =}')


def power(x, y, /, mod=None):
    r = x ** y
    if mod is not None:
        r %= mod
    return r 

print(f'{power(4, 2)     =}')
print(f'{power(4, 2, 10) =}')
print(f'{power(4, 2, mod=10) =}')
# print(f'{power(x=4, y=2, mod=10) =}')
# SyntaxError: positional argument follows keyword argument