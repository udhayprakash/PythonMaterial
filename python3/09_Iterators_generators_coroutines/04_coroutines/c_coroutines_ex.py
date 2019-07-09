def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

# Creating generator/co-routine 
it = minimize()

# Start the generator/co-routine
next(it) 

# Passing values
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

# closing co-routine
it.close()