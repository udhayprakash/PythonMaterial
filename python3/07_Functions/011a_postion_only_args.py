#!/usr/bin/python
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


def multiply_then_add(a, b, c, /, d=10):
    return a + b + c + d


multiply_then_add(5, 10, 20)
multiply_then_add(5, 10, 20, 89)
multiply_then_add(5, 10, 20, d=89)

# multiply_then_add(5, 10, x=20)
# TypeError: multiply_then_add() got an unexpected keyword argument 'x'


def power(x, y, /, mod=None):
    """
    All parameters to the left of / (in this case, x and y) can only be passed positionally.
    mod can be passed positionally or with a keyword.
    >>> pow(2, 10)  # valid
    >>> pow(2, 10, 17)  # valid
    >>> pow(2, 10, mod=17)  # valid
    >>> pow(x=2, y=10)  # invalid, will raise a TypeError
    >>> pow(2, y=10)  # invalid, will raise a TypeError
    """
    r = x ** y
    if mod is not None:
        r %= mod
    return r
