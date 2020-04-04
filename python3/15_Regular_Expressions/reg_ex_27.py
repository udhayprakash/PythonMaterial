#!/usr/bin/python
"""
purpose: regular expression  demo 

"""

import re

print(re.findall(r'\w+', 'fox:αλεπού'))
print(re.findall(r'\w+', 'fox:αλεπού', flags=re.A))
print(re.findall(r'[a-zA-Z0-9_]+', 'fox:αλεπού'))
print(re.search(r'[a-zA-Z]', 'İıſK'))  # False
print(re.search(r'[a-z]+', 'İıſK', flags=re.I)[0])
print(re.search(r'[a-z]', 'İıſK', flags=re.I | re.A))  # False

import regex

print(regex.findall(r'\p{L}+', 'fox:αλεπού,eagle:αετός'))
print(regex.findall(r'\p{Greek}+', 'fox:αλεπού,eagle:αετός'))
print(regex.findall(r'\p{Word}+', 'φοο12,βτ_4,foo'))
print(regex.sub(r'\P{L}+', r'', 'φοο12,βτ_4,foo'))

print([hex(ord(c)) for c in 'fox'])
print([c.encode('unicode_escape') for c in 'αλεπού'])
print([c.encode('unicode_escape') for c in 'İıſK'])
print(re.findall(r'[\u0061-\u007a]+', 'fox:αλεπού,eagle:αετός'))

