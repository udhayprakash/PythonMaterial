"""
Purpose: Using regex Module

    Install the regex module if not already installed

        pip install -U regex --user

"""
import re

import regex

# \p - presence of
# \P - absence of
# L - latin
print(regex.findall(r"\p{L}+", "fox:αλεπού,eagle:αετός"))
print(regex.findall(r"\p{Greek}+", "fox:αλεπού,eagle:αετός"))
print(regex.findall(r"\p{Word}+", "φοο12,βτ_4,foo"))
print(regex.sub(r"\P{L}+", r"", "φοο12,βτ_4,foo"))
print()

print(re.findall(r"[[:word:]]+", "fox:αλεπού,eagle:αετός", flags=re.A))
print(regex.findall(r"[[:word:]]+", "fox:αλεπού,eagle:αετός", flags=re.A))
print(regex.findall(r"[[:word:]]+", "fox:αλεπού,eagle:αετός", flags=regex.A))
print()

print(regex.split(r"[[:digit:]]+", "Sample123string42with777numbers"))
print(regex.findall(r"[[:alpha:]]+", "Sample123string42with777numbers"))
print(regex.findall(r"[[:word:][:space:]]+", "tea sea-pit sit-lean bean"))
print(regex.findall(r"[[:^space:]]+", "tea sea-pit sit-lean bean"))
print(regex.findall(r"(?<![[:punct:]])\b\w+\b(?![[:punct:]])", "tie. ink eat;"))
print(re.findall(r"\b[^aeiou]+\b", "tryst glyph pity why"))
print()

print(regex.findall(r"(?V1)\b[a-z&&[^aeiou]]+\b", "tryst glyph pity why"))
print(regex.findall(r"(?V1)\b[[a-l]~~[g-z]]+\b", "gets eat top sigh"))
print()

para = '"Hi", there! How *are* you? All fine here.'
print(regex.sub(r"(?V1)[[:punct:]--[.!?]]+", r"", para))
print()

words = "tiger imp goat eagle rat"
print(regex.sub(r"\b(?:imp|rat)\b(*SKIP)(*F)|[a-z]++", r"(\g<0>)", words))
print()

row = '1,"cat,12",nice,two,"dog,5"'
print(regex.sub(r'"[^"]++"(*SKIP)(*F)|,', r"|", row))
