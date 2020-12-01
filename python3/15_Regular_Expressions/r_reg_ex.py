#!/usr/bin/python3
"""
purpose: regular expression

\d - presence of any digit 0-9
\D - absence of any digit
\w - presence of any alphanumeric a-z A-Z 0-9
\W - absence of any alphanumeric
\s  -presence of  white space AND \n
\S  - absence of white space and \n
"""

import re

print(re.search('[a-z]+', 'Udhay Prakash').group())
print(re.search('[a-zA-Z0-9]+', 'Udhay Prakash').group())
print(re.search(r'\w+', 'Udhay Prakash').group())
print()

print(re.search(r'\w+\W\w', 'Udhay Prakash').group())
print(re.search(r'\w+\W\w+', 'Udhay Prakash').group())
print(re.search(r'\w+\s\w+', 'Udhay Prakash').group())

# Grouping in regular expressions
print(re.search(r'(\w+)\s(\w+)', 'Udhay Prakash').group())
print(re.search(r'(\w+)\s(\w+)', 'Udhay Prakash').group(0))
#                                  1       2
print(re.search(r'(\w+)\s(\w+)', 'Udhay Prakash').group(1))  # Udhay
print(re.search(r'(\w+)\s(\w+)', 'Udhay Prakash').group(2))  # Prakash
print()


print(re.search(r'(\w+)\W(\w+)', 'Udhay Prakash').groups())
# ('Udhay', 'Prakash')
