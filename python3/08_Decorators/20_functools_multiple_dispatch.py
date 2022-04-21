from multipledispatch import dispatch

# pip install multipledispatch

# Useful for dispatching based on multiple arguments


@dispatch(list, str)
def concatenate(a, b):
    a.append(b)
    return a


@dispatch(str, str)
def concatenate(a, b):
    return a + b


@dispatch(str, int)
def concatenate(a, b):
    return a + str(b)


print(concatenate(['a', 'b'], 'c'))
# ['a', 'b', 'c']
print(concatenate('Hello', 'World'))
# HelloWorld
print(concatenate('a', 1))
# a1
