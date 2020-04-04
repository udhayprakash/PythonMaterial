#!/usr/bin/python
"""
Purpose: Regular Expressions

    .  any character, except newline
    \d - presence of any digit 0-9
    \D - absence of any digit
    \w - presence of any alphanumeric a-z A-Z 0-9
    \W - absence of any alphanumeric a-z A-Z 0-9
    \s  -presence of  white space AND \n
    \S  - absence of white space and \n
"""

import re

print(re.search(r'\d', '150').group())  # 1
print(re.search(r'\d*', '150').group())  # 150
print(re.search(r'\d+', '150').group())  # 150
print(re.search(r'\d?', '150').group())  # 1

print(re.search(r'\d', 'cost of apples is $150 per basket').group())  # 1
print(re.search(r'\d*', 'cost of apples is $150 per basket').group())  # 150
print(re.search(r'\d+', 'cost of apples is $150 per basket').group())  # 150
print(re.search(r'\d?', 'cost of apples is $150 per basket').group())  # 1

# re.match() -> to get a pattern at first of search string
# re.match() -> to get a pattern at any place in search string

# re.findall() -> to get all the patterns within the search string
print(re.findall('python', 'PYTHON python PYTHon pYTHon43454'))
print(re.findall('python', 'PYTHON python PYTHon pYTHon43454', re.I))

target_string = '''
Hi everyone!
The PARTY is on 23rd of May 2020, at xyz place. at time 7.30 pm IST
And the RECEPTION is on 30th of May, 2020 at xxx place.
Thanks
'''
print(re.findall('2', target_string, re.I))
print(re.findall('2020', target_string, re.I))

print(re.findall(r'\d', target_string))
# print(re.findall(r'\d*', target_string))
print(re.findall(r'\d+', target_string))

print(re.findall('[0-9]', target_string))  # ['2', '3', '2', '0', '2', '0', '7', '3', '0', '3', '0', '2', '0', '2', '0']
print(re.findall('[0-9]+', target_string))  # ['23', '2020', '7', '30', '30', '2020']

print(re.findall('[1-5]', target_string))  # ['2', '3', '2', '2', '3', '3', '2', '2']
print(re.findall('[1-5]+', target_string))  # ['23', '2', '2', '3', '3', '2', '2']

print()
print(re.findall(r'\w', target_string))
# ['H', 'i', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e', 'T', 'h', 'e', 'P', 'A', 'R', 'T', 'Y', 'i', 's', 'o', 'n', '2', '3', 'r', 'd', 'o', 'f', 'M', 'a', 'y', '2', '0', '2', '0', 'a', 't', 'x', 'y', 'z', 'p', 'l', 'a', 'c', 'e', 'a', 't', 't', 'i', 'm', 'e', '7', '3', '0', 'p', 'm', 'I', 'S', 'T', 'A', 'n', 'd', 't', 'h', 'e', 'R', 'E', 'C', 'E', 'P', 'T', 'I', 'O', 'N', 'i', 's', 'o', 'n', '3', '0', 't', 'h', 'o', 'f', 'M', 'a', 'y', '2', '0', '2', '0', 'a', 't', 'x', 'x', 'x', 'p', 'l', 'a', 'c', 'e', 'T', 'h', 'a', 'n', 'k', 's']
print(re.findall(r'\w+', target_string))
# ['Hi', 'everyone', 'The', 'PARTY', 'is', 'on', '23rd', 'of', 'May', '2020', 'at', 'xyz', 'place', 'at', 'time', '7', '30', 'pm', 'IST', 'And', 'the', 'RECEPTION', 'is', 'on', '30th', 'of', 'May', '2020', 'at', 'xxx', 'place', 'Thanks']

print(re.findall('[a-z]', target_string))
# ['i', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e', 'h', 'e', 'i', 's', 'o', 'n', 'r', 'd', 'o', 'f', 'a', 'y', 'a', 't', 'x', 'y', 'z', 'p', 'l', 'a', 'c', 'e', 'a', 't', 't', 'i', 'm', 'e', 'p', 'm', 'n', 'd', 't', 'h', 'e', 'i', 's', 'o', 'n', 't', 'h', 'o', 'f', 'a', 'y', 'a', 't', 'x', 'x', 'x', 'p', 'l', 'a', 'c', 'e', 'h', 'a', 'n', 'k', 's']
print(re.findall('[A-Z]', target_string))
['H', 'T', 'P', 'A', 'R', 'T', 'Y', 'M', 'I', 'S', 'T', 'A', 'R', 'E', 'C', 'E', 'P', 'T', 'I', 'O', 'N', 'M', 'T']

print(re.findall('[aeiou]', target_string, re.I))
# ['i', 'e', 'e', 'o', 'e', 'e', 'A', 'i', 'o', 'o', 'a', 'a', 'a', 'e', 'a', 'i', 'e', 'I', 'A', 'e', 'E', 'E', 'I', 'O', 'i', 'o', 'o', 'a', 'a', 'a', 'e', 'a']

print(re.findall('[a-zA-Z]+', target_string))
# ['Hi', 'everyone', 'The', 'PARTY', 'is', 'on', 'rd', 'of', 'May', 'at', 'xyz', 'place', 'at', 'time', 'pm', 'IST', 'And', 'the', 'RECEPTION', 'is', 'on', 'th', 'of', 'May', 'at', 'xxx', 'place', 'Thanks']

print(re.findall('[a-zA-Z0-9]+', target_string))
print(re.findall('\w+', target_string))
# ['Hi', 'everyone', 'The', 'PARTY', 'is', 'on', '23rd', 'of', 'May', '2020', 'at', 'xyz', 'place', 'at', 'time', '7', '30', 'pm', 'IST', 'And', 'the', 'RECEPTION', 'is', 'on', '30th', 'of', 'May', '2020', 'at', 'xxx', 'place', 'Thanks']


print()
print(re.findall(r'\s+', target_string))
# ['\n', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', '\n']
