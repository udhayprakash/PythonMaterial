def foo(word='world'):
    """
    >>> foo()
    hello ...

    >>> foo()
    hello world

    >>> foo('brother')
    hello brother
    
    """
    print("hello " + word)

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    # doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)