#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/


def outer(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            return e
        else:
            return func(*args, **kwargs)

    return inner

############################################
def div(a, b):
    return a / b


foo = outer(div)
print foo(4, 2)
print foo(4, 0)

###############################################

def addition(m,n):
    return m + n

result = outer(addition)
print result(2, 4)
print result('2', 4)