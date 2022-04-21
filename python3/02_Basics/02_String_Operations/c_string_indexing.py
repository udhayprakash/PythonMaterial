#!/usr/bin/python3
"""
Purpose: String Operations
            - Indexing
"""
language = "Python Programming"
print(language, type(language))

# len() - to get no. of characters in string
print("len(language)=", len(language))

print("STRING OPERATIONS")
print("--------------------------------------")
print("string Indexing")

# P   y  t  h  o n   P r  o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8  9 10 11 12 13 14 15 16 17    - forward indexing
# -18                    -9 -8 -7 -6 -5 -4 -3 -2 -1    - reverse indexing

# NOTE: indexing starts with 0

print("language    :", language)
print("language[14]:", language[14])
print("language[6] :", language[6])
print("language[17]:", language[17])

# print('language[18]:', language[18])
# IndexError: string index out of range

print()
print("language[0]   :", language[0])
print("language[-0]  :", language[-0])

print()
print("language[-3]  :", language[-3])
print("len(language) :", len(language))
print("language[len(language)-3]  :", language[len(language) - 3])

print()
print("language[-18] :", language[-18])
print("language[0]   :", language[0])

# print('language[-19] :', language[-19])
# IndexError: string index out of range

# NOTE 1: For a string of length N,
# we can indexing from -N to (N -1)

# print('language[0.0]   :', language[0.0])
# TypeError: string indices must be integers
