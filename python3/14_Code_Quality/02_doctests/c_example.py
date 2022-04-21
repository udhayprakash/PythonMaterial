#!/usr/bin/python

def hello(name='world!'):
    """
    >>> hello()
    Hello world!

    >>> hello()
    Hello ...

    >>> hello('Michel')
    Hello Michel
    """
    print(f'Hello {name}')



if __name__ == '__main__':
    import doctest

    # doctest.testmod()
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    # doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
