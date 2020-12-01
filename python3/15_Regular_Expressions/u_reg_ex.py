#!/usr/bin/python3
"""
Purpose: Regular Expressions

Pattern repetition
    {}  specifies the number of times, the previous character should present

Mid-way between greedy and non-greedy patterns
"""

import re

print(re.findall('ab{0}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))
print(re.findall('ab{2}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))
print(re.findall('ab{5}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))

# range of repetition
print(re.findall('ab{2,5}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))
