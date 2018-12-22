def simple_math(x, y):
    '''
    This function will return x + y
    we can use it on numbers. Passing 1 and 2:

    >>> simple_math(1, 2)
    3

    We should get 3 as a return value

    It will also work on strings. Passing the strings 'k' and 'v':

    >>> simple_math('k', 'v')
    'kv'
    
    We should get 'kv'
    '''
    return x + y


class SimpleClass():
    pass

def class_testing_method_ahoy(obj):
    ''' Should return a list containing the object

    >>> class_testing_method_ahoy(SimpleClass()) # doctest: +ELLIPSIS
    [<simple_doctest.SimpleClass object at 0x...>]
    '''

    return [obj]
    
