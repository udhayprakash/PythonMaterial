#!/usr/bin/python
'''
Purpose: Demonstration of the importance of Decorators
Ref: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
'''

def outer(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            return e
        else:
            return func(*args, **kwargs)

    return inner


def div(a, b):
    return a / b


print(div(10,3))
print(div(10,2.5))
# print div(10,0)

foo = outer(div)
foo(10,3)

print(outer(div(10,2.5)))



@outer         # comment this line and observe difference
def div(a, b):
    return a / b

print(div(4, 2))
print(div(4, 0))



@outer
def add(a, b):
    return a + b



print(add(2, 3))
print(add('a', 3))
