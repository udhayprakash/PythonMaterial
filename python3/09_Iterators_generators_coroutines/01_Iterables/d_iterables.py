#!/usr/bin/python
"""
Purpose:

sorted()
"""

numbers = [5, 2, 3, 1, 4]
print(f'numbers         : {numbers}')
print()
print(f'sorted(numbers) : {sorted(numbers)}')
print(f'numbers         : {numbers}')

# NOTE: sorted() will create new objects. 
# existing objects is not modified.
print()

numbers.sort() # updates the original object
print(f'numbers         : {numbers}')

print()
print(f'sorted(numbers) : {sorted(numbers)}')
print(f'sorted(numbers, reverse=True) : {sorted(numbers, reverse=True)}')

print()
print(f'reversed(numbers): {reversed(numbers)}')
revr_numbers = list(reversed(numbers))
print(f'revr_numbers     : {revr_numbers}')

print()
word = "Python "
print(f'word        :{word}')
print(f'list(word)  :{list(word)}')
print(f'sorted(word):{sorted(word)}')

print()
lst_of_strs = 'Apple is a fruit'.split()
print(lst_of_strs)
print(sorted(lst_of_strs))
print(sorted(lst_of_strs, key=str.lower))

print()
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))  # [1, 2, 3, 4, 5]
