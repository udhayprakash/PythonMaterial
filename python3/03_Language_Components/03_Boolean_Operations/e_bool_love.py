#!/usr/bin/python3

import this

# print(this)

love = this

# is --- object level equivalence check
print(f'{this == love         =}')
print(f'{id(this) == id(love) =}')
print(f'{id(this)             =}')
print(f'{id(love)             =}')
print()

print(f'{this is love         =}')
# print(f'{this not is love         =}')
# SyntaxError: f-string: invalid syntax

print(f'{this is not love     =}')
print(f'{not this is love     =}')
print()

print(f'{this is love         =}')
print(f'{love is love         =}')
print(f'{love is not True or False=}')
print(f'{love is not (True or False)=}')  # PEDMAS
