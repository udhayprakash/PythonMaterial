#!/usr/bin/python3
"""
Purpose: working with Iterables 
"""
values = [1, 2, 3, 4, 2, 1, 3, 1, 4, 3, 3]
print(f'{values                        =}')
print()

print(f'{max(values)                   =}')
print(f'{max(values, key=values.count) =}') # mode
print()

print(f'{min(values)                   =}')
print(f'{min(values, key=values.count) =}')
print()


print(f'{sum(values)                   =}')
print(f'{sum(values, start=0         ) =}') # +0
print(f'{sum(values, start=4         ) =}') # +4
print(f'{sum(values, start=100       ) =}') # +100
print()

print(f'{sorted(values)                                  =}')
print(f'{sorted(values, key=values.count)                =}')
print(f'{sorted(values, key=values.count, reverse=True)  =}')
print(f'{sorted(values, key=values.count, reverse=False) =}')
print()


# word = 'malayalam'
# print(f'{word                       = }')
# print(f'{max(word)                  = }')
# print(f'{min(word)                  = }')

# print(f'{max(word, key=values.count)  = }')
# print(f'{min(word, key=values.count)  = }')

# print(f'{max(list(word), key=values.count)  = }')
# print(f'{min(list(word), key=values.count)  = }')