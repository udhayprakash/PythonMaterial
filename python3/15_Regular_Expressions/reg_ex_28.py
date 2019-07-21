#!/usr/bin/python
"""
purpose: regular expression  demo 

"""

import re 

print(re.findall(r'\w+', 'fox:αλεπού'))
print(re.findall(r'\w+', 'fox:αλεπού', flags=re.A))
print(re.findall(r'[a-zA-Z0-9_]+', 'fox:αλεπού'))
print(re.search(r'[a-zA-Z]', 'İıſK')) # False
print(re.search(r'[a-z]+', 'İıſK', flags=re.I)[0])
print(re.search(r'[a-z]', 'İıſK', flags=re.I|re.A)) #False

import regex 
print(regex.findall(r'\p{L}+', 'fox:αλεπού,eagle:αετός'))
print(regex.findall(r'\p{Greek}+', 'fox:αλεπού,eagle:αετός'))
print(regex.findall(r'\p{Word}+', 'φοο12,βτ_4,foo'))
print(regex.sub(r'\P{L}+', r'', 'φοο12,βτ_4,foo'))

print([hex(ord(c)) for c in 'fox'])
print([c.encode('unicode_escape') for c in 'αλεπού'])
print([c.encode('unicode_escape') for c in 'İıſK'])
print(re.findall(r'[\u0061-\u007a]+', 'fox:αλεπού,eagle:αετός'))



import re

x1 = re.search(r"\w+", u"♥αβγ!", re.U)
x2 = re.search(r"\w+", u"♥αβγ!")

if x1:
    print(x1.group().encode("utf-8")) # → 「αβγ」
else:
    print('no match')

print(x2)



d = { 'hand': 1, 'handy': 2, 'handful': 3, 'a^b': 4 }

words = [re.escape(k) for k in d.keys()]
print(words)

re.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=re.A)

regex.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=re.A)

regex.findall(r'[[:word:]]+', 'fox:αλεπού,eagle:αετός', flags=regex.A)

print(regex.split(r'[[:digit:]]+', 'Sample123string42with777numbers'))
print(regex.findall(r'[[:alpha:]]+', 'Sample123string42with777numbers'))
print(regex.findall(r'[[:word:][:space:]]+', 'tea sea-pit sit-lean bean'))
print(regex.findall(r'[[:^space:]]+', 'tea sea-pit sit-lean bean'))
print(regex.findall(r'(?<![[:punct:]])\b\w+\b(?![[:punct:]])', 'tie. ink eat;'))
print(re.findall(r'\b[^aeiou]+\b', 'tryst glyph pity why'))

regex.findall(r'(?V1)\b[a-z&&[^aeiou]]+\b', 'tryst glyph pity why')

regex.findall(r'(?V1)\b[[a-l]~~[g-z]]+\b', 'gets eat top sigh')

para = '"Hi", there! How *are* you? All fine here.'

regex.sub(r'(?V1)[[:punct:]--[.!?]]+', r'', para)

words = 'tiger imp goat eagle rat'

regex.sub(r'\b(?:imp|rat)\b(*SKIP)(*F)|[a-z]++', r'(\g<0>)', words)

row = '1,"cat,12",nice,two,"dog,5"'

regex.sub(r'"[^"]++"(*SKIP)(*F)|,', r'|', row)