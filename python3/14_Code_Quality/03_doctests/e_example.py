"""
Purpose:

"""
import doctest


def power(x, y, /, mod=None):
    """
    All parameters to the left of / (in this case, x and y) can only be passed positionally.
    mod can be passed positionally or with a keyword.
    >>> power(2, 10)
    1024
    >>> power(2, 10, 17)
    4
    >>> power(2, 10, mod=17)
    4
    >>> power(x=2, y=10)
    Traceback (most recent call last):
    ...
    TypeError: power() got some positional-only arguments passed as keyword arguments: 'x, y'
    >>> power(2, y=10)
    Traceback (most recent call last):
    ...
    TypeError: power() got some positional-only arguments passed as keyword arguments: 'y'
    """
    r = x**y
    if mod is not None:
        r %= mod
    return r


if __name__ == "__main__":
    # doctest.testmod()
    doctest.testmod(optionflags=doctest.ELLIPSIS)


# - python -m doctest e_example.py

# Assigment : Generators check
