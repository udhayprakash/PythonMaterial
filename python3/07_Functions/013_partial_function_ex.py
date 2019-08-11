# ordinary function
def multiply(x,y):
   return x * y

print(multiply(2, 4))
print(multiply(2, 14))
print(multiply(2, 2))

##############################################
# partial function
import functools

# create a new function that multiplies by 2
dbl = functools.partial(multiply,2)

print('dbl', dbl)
print('type(dbl)', type(dbl))

print(dbl(4))           # multiply(2, 4)
print(dbl(14))          # multiply(2, 14)
print(dbl(3))           # multiply(2, 3)
