#!/usr/bin/python3
"""
Purpose: Iterators
"""
# list to iterator -> list iterator
alpha = ["a", "e", "i", "o", "u"]
print(type(alpha), alpha)

alpha_it = iter(alpha)
print(type(alpha_it), alpha_it)

print()
# tuple to iterator -> tuple iterator
alpha = ("a", "e", "i", "o", "u")
print(type(alpha), alpha)

alpha_it = iter(alpha)
print(type(alpha_it), alpha_it)

print()
# set to iterator -> set iterator
alpha = {"a", "e", "i", "o", "u"}
print(type(alpha), alpha)

alpha_it = iter(alpha)
print(type(alpha_it), alpha_it)  # set_iterator

print()
alpha = {"a": 1, "e": 2, "i": 3, "o": 4}
print(type(alpha), alpha)

alpha_it = iter(alpha)
print(type(alpha_it), alpha_it)  # dict_keyiterator

alpha_it = iter(alpha.keys())
print(type(alpha_it), alpha_it)  # dict_keyiterator

alpha_it = iter(alpha.values())
print(type(alpha_it), alpha_it)  # dict_valueiterator

alpha_it = iter(alpha.items())
print(type(alpha_it), alpha_it)  # dict_itemiterator

print()
language = "python"
language_it = iter(language)
print(type(language_it), language_it)  # str_iterator
