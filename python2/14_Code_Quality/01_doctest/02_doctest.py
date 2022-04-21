def foo():
    """
    >>> foo()
    hello ...
    """
    print('hello world')

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
