#!/usr/bin/python
"""
purpose: regular expression  demo 

Pattern repetion

{}  specifies the number of times, the previous character should present
"""

import re 
print(re.findall('ab{0}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))
print(re.findall('ab{2}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))
print(re.findall('ab{5}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))

# range of repetition
print(re.findall('ab{2,5}', 'a ab abb abbbb abbbbbbb abbbbbbbbbb'))


