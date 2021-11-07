#!/usr/bin/python3
"""
Purpose:
     Python uses Timsort algorithm for sorting list.sort()
sorted()
    - applicable on any iterable object
    - create new list object and stores sorted result there
    - default sorting is in ascending order
reversed()
    - results in an lazy object
    - reverses the elements in reverse order of ASSIGNMENT
"""

numbers = [5, 2, 3, 1, 4]
print(f'numbers         : {numbers}')

print()
print(f'sorted(numbers) : {sorted(numbers)}')
print(f'numbers         : {numbers}')

# NOTE: sorted() will create new objects.
# existing objects is not modified.
print()

numbers.sort()  # updates the original object
print(f'numbers         : {numbers}')

print()
print(f'sorted(numbers)                 : {sorted(numbers)}')
print(f'sorted(numbers, reverse=True)   : {sorted(numbers, reverse=True)}')
numbers.sort(reverse=True)
print(f'numbers                         : {numbers}')

print()
numbers = [5, 2, 3, 1, 4]
print(f'reversed(numbers): {reversed(numbers)}')  # list_reverseiterator
revr_numbers = list(reversed(numbers))
print(f'revr_numbers     : {revr_numbers}')  # [4, 1, 3, 2, 5]

# ------------------------------------------
print()
word = "az AZ 10"
print(f'word                        :{word}')
print(f'list(word)                  :{list(word)}')
print(f'sorted(word)                :{sorted(word)}')
print(f'sorted(word, key=str.lower) :{sorted(word, key=str.lower)}')

print()
lst_of_strs = 'Apple is a fruit'.split()
print(lst_of_strs)
print(sorted(lst_of_strs))
print(sorted(lst_of_strs, key=str.lower))

# -----------------------------------------
print()
my_dict = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(my_dict))  # [1, 2, 3, 4, 5]
print(sorted(my_dict.keys()))  # [1, 2, 3, 4, 5]
print(sorted(my_dict.values()))  # ['A', 'B', 'B', 'D', 'E']
print()
print(sorted(my_dict.items()))  # [(1, 'D'), (2, 'B'), (3, 'B'), (4, 'E'), (5, 'A')]
print(sorted(my_dict.items(), key=lambda x: x[0]))  # by key
print(sorted(my_dict.items(), key=lambda x: x[1]))  # by value
print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))  # by value
