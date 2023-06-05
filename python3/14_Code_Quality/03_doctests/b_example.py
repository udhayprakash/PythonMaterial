import doctest


def add_two_numbers(m, n):
    """
    Returns the sum of the given two numbers.

    >>> add_two_numbers(12, 34)
    46
    >>> add_two_numbers('12', '34')
    46
    >>> add_two_numbers(12, '34')
    46
    >>> add_two_numbers('12', 34)
    46
    >>> add_two_numbers(12.0, 34.00000000)
    46
    """
    # return m + n
    return int(m) + int(n)


if __name__ == "__main__":
    doctest.testmod()
