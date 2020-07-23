x = range(1, 20)

print x[1:20:3] # [2, 5, 8, 11, 14, 17]

print x[slice(1, 20, 3)] # [2, 5, 8, 11, 14, 17]

print slice(1, 20, 3) # slice(1, 20, 3)


language = "python Programming"
print language
print language[2:]
print language[slice(2, None, 1)]