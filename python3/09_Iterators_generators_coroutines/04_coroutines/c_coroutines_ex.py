def minimize():
    current = yield #999999999999999999
    while True:
        value = yield current
        current = min(value, current)

# Creating generator/co-routine 
it = minimize()

# Start the generator/co-routine
print(next(it)) 

# Passing values
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

# closing co-routine
it.close()