


def my_generator():
    print(' I am in the function')
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    

m = my_generator()
print(m)

print(next(m))
print(next(m))
print(next(m))
print(next(m))

print(next(m))