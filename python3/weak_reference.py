import weakref
print(dir(weakref))

class A:
    pass

a = A()
b = weakref.ref(a)
c= weakref.ref(a)
print(f'{id(a) =}')
print(f'{id(b) =}')
print(f'{id(c) =}')

assert b is c 
assert b is a.__weakref__
print(weakref.getweakrefs(a))