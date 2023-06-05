"""
Purpose: Adding doctest
"""
import doctest


def square(x):
    """
        This function will return the square value of given value.
    >>> square(9)
    81
    >>> square(-9)
    81
    >>> square(0.09)
    0.0081
    >>> square(0.009)
    8.099999999999999e-05
    >>> square(-0.009)
    8.099999999999999e-05
    """
    return x * x


if __name__ == "__main__":
    doctest.testmod()

    print(f"{square(2) =}")
