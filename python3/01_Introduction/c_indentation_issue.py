#!/usr/bin/python


print("hello world")   
print('hello world')  # IndentationError: unexpected indent



# block code - if, elif , for,  while, class,  functions


if 2 < 3:
    print('2 < 3') # IndentationError: expected an indented block

if 12> 23:
    print('12> 23')
else:
    print('else condition')

if 12> 23:
    print('12> 23')
elif 23>34:
    print('23>34')
elif 34==34:
    print('34==34')
else:
    print('else condition')


if 2 < 3:
    if 2 < 6:
        if 2 < 62:
            print('2 < 3 < 6')
    print()

for i in range(9):
    print(i)

# for i in range(9):
# print(i)   # IndentationError: expected an indented block


# tabs vs white-space
# PEP 8 (Python Enhancement Proposal) - code style guide
# four white-spaces