#!/usr/bin/python3
"""
Purpose: String Module
"""
import string

print(string.__doc__)

print(f'{string.ascii_letters   =}')
print(f'{string.ascii_lowercase =}')
print(f'{string.ascii_uppercase =}')
print(f'{string.digits          =}')
print(f'{string.hexdigits       =}')
print(f'{string.octdigits       =}')
print(f'{string.printable       =}')
print(f'{string.punctuation     =}')
print(f'{string.whitespace      =}')
print()

print(f'{string.capwords("aaaaaaaaaaaaaaaaa")=}')
print(f'{string.capwords("11111111111111111")=}')
print(f'{string.capwords("one two three 345")=}')
print()

s = "let us capitalize every word of this sentence."
print(string.capwords(s))
