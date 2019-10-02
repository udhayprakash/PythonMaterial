#!/usr/bin/env python

# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a commaseparated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world Then, the output should be: bag,hello,without,world

a = eval(input("Enter words,separated with comma:"))
a = list(a)
print(a)
a.sort()
print(a)
for i in a:
    print(i, end=' ')
