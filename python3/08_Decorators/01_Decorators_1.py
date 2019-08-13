#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def div(a, b):
    return a / b

# print(div(4, 2))
# print(div(4, 0))

def outer(func):
    def inner(a, b):
        # print(f'In inner(), func:{func}') 
        try:
            func(a, b)          # div(), add()
        except Exception as ex:
            return repr(ex)
        else:
            return func(a, b)   # div(), add()
    return inner

# inner()

result = outer(div)
# print(type(result), result) # reference to inner()

print(result(4, 2))
print(result(4, 0))
print()

def add(n1, n2):
    return n1 + n2 

temp_var = outer(add)  # refence  to inner
print('temp_var(2, 3)  ', temp_var(2, 3))
print("temp_var('a', 3)", temp_var('a', 3))
