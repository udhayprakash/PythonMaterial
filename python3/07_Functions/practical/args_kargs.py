# *-* encoding=utf-8 *-*
'''
just try to use *args and **kargs.
'''

def foo(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('---------------------------------------')

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)