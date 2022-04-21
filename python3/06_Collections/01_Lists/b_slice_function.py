#!/usr/bin/python3
"""
Purpose: slice() function
"""
x = range(1, 20)
print(f"{type(x)} {x =}")

# LIST() - BUILT-IN FUNCTION
x = list(range(1, 20))
print(f"{type(x)} {x =}")

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]   values
#  0  1  2  3  4  5  6  7  8  9   10, 11, 12, 13, 14, 15, 16, 17, 18   forward indices

print()
print(x[1:20:3])  # [2, 5, 8, 11, 14, 17]  values at that position
print(x[slice(1, 20, 3)])  # [2, 5, 8, 11, 14, 17]
assert x[1:20:3] == x[slice(1, 20, 3)]

# -----------------------------------------------------
print(slice(1, 20, 3))  # slice(1, 20, 3)

language = "python Programming"
print("language                     ", language)
print("language[2:]                 ", language[2:])
print("language[slice(2, None, 1)]  ", language[slice(2, None, 1)])

assert language[2:] == language[slice(2, None, 1)]
assert language[:] == language[slice(None, None, None)]
assert language[::] == language[slice(None, None, None)]
assert language[::1] == language[slice(None, None, 1)]
assert language[::-1] == language[slice(None, None, -1)]
