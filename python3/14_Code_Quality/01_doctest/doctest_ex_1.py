import doctest


def square(x):
    """Return the square of x.
    >>> square(4)
    16
    >>> square(-4)
    16
    >>> square(0.2)
    0.04000000000000001
    """

    return x * x


if __name__ == '__main__':
    doctest.testmod()
