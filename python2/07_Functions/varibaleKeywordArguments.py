#!/usr/bin/python

'''
    Purpose: Demonstration of the usage of *args and **kwargs

    *args   stores variables in tuple
    ** kwargs stores variables in dictionaries

'''


def foo(firstArg, *args, **kwargs):
    print('Necessary argument is ', firstArg)
    print('args = ', args)
    print('type(args) is', type(args))
    if args:
        for arg in args:
            print(arg)

    print('kwargs = ', kwargs)
    print('type(kwargs) is', type(kwargs))
    if kwargs:
        print('The keyword arguments are\n', end=' ')
        # for kwarg in kwargs:
        #    print kwarg
        for k, v in list(kwargs.items()):
            print('%15r  --> %10r' % (k, v))


if __name__ == '__main__':
    print('\n', '_' * 70)
    foo(321)
    print('\n', '_' * 70)
    foo(1, 2, 3, 4)
    print('\n', '_' * 70)
    foo(99, 22.0, True, [12, 34, 56])
    print('\n', '_' * 70)
    foo(32, 56, 32, (2, [34, (2.3, 99, 0)]))
    print('\n', '_' * 70)
    foo(2.0, a=1, b=2, c=3)
    print('\n', '_' * 70)
    foo('a', 1, None, a=1, b='2', c=3)
    print('\n', '_' * 70)
    foo(123, courseName='Python', currentStatus='40% completed', studentList=['Yash', 'Michel', 'Johson'])
