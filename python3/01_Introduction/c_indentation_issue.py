#!/usr/bin/python
"""
Purpose: Importance of Indendation
"""
print('Hello World')
#    print('hello World 2')  # IndentationError: unexpected indent
print('hello World 2')


# block code - if, else, elif, for, while, def , class, ...
# if 12 > 3:
# print('greater')            #IndentationError: expected an indented block

if 12 > 3:
    print('greater')

if 12 > 34:
    print('greater')
else:
    print('It is lesser')

if 1 < 2:
    print('case 1')
elif 2 > 1:
    print('case 2')
else:
    print('case 3')


if 1 < 2:
    if 2 < 3:
        if 3 < 4:
            if 4 < 5:
                print('LESSER')
        else:
            print('something')
    else:
        print('something')


for i in range(9):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, '*', j, '=', i * j)
        j += 1
    print()
    i += 1


def my_func():
    return "hello world"


class MyClass:
    def __init__(self):
        pass

# tabs vs white-space
# PEP 8 (Python Enhancement Proposal) - code style guide
# Prefer white-spaces, to tabs; four white-spaces
