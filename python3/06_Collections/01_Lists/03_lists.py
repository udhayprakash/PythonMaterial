x = list(range(1, 20))

print(x)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#  0  1  2 ...

print(x[1:20:3])            # [2, 5, 8, 11, 14, 17]

print(x[slice(1, 20, 3)])   # [2, 5, 8, 11, 14, 17]

assert x[1:20:3] == x[slice(1, 20, 3)]


print(slice(1, 20, 3)) # slice(1, 20, 3)


language = "python Programming"
print(language)
print(language[2:])
print(language[slice(2, None, 1)])

assert language[2:] == language[slice(2, None, 1)]