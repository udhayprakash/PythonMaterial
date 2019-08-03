#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def div(a, b):
    return a / b

# print(div(4, 2))
# print(div(4, 0))

def outer(func):  # func-addition
    def inner(num1, num2): #*args, **kwargs):
        try:
            func(num1, num2) #*args, **kwargs)
        except Exception as e:
            return e
        else:
            return func(num1, num2) #*args, **kwargs)
    
    return inner

############################################
foo = outer(div)# foo-inner
print('foo', foo)
print(foo(4, 2))
print(foo(4, 0))

###############################################

def addition(m,n):
    return m + n

result = outer(addition)  #  result-inner
print(result(2, 4))       # inner(2, 4)
print(result('2', 4))