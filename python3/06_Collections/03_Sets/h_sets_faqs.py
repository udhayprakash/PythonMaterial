#!/usr/bin/python3
"""
Purpose: sets FAQs
"""

my_set = {1, True, int(1.2)}
print(f"{my_set =}")

my_set = {True, int(1.2), 1}
print(f"{my_set =}")

my_set = {int(1.2), 1, True}
print(f"{my_set =}")

print()
my_set = {0, False, 2 + 3 == 6}
print(f"{my_set =}")

my_set = {False, 2 + 3 == 6, 0}
print(f"{my_set =}")

my_set = {2 + 3 == 6, 0, False}
print(f"{my_set =}")

# NOTE:
# 1. True, False has values of 1, 0 respectively
# 2. Whichever value is placed first in definition,
#    that will come in the output
