from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)

print('dbl', dbl)
print('type(dbl)', type(dbl))

print(dbl(4))
print(dbl(14))
print(dbl(3))
