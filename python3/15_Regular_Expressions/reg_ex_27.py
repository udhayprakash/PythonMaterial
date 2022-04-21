#!/usr/bin/python
"""
purpose: regular expression  demo

"""

import re

print(re.findall(r"\w+", "fox:αλεπού"))
print(re.findall(r"\w+", "fox:αλεπού", flags=re.A))  # ASCII only
print(re.findall(r"[a-zA-Z0-9_]+", "fox:αλεπού"))
print(re.search(r"[a-zA-Z]", "İıſK"))  # False
print(re.search(r"[a-z]+", "İıſK", flags=re.I)[0])
print(re.search(r"[a-z]", "İıſK", flags=re.I | re.A))  # False
print()

print([hex(ord(c)) for c in "fox"])
print([c.encode("unicode_escape") for c in "αλεπού"])
print([c.encode("unicode_escape") for c in "İıſK"])
print(re.findall(r"[\u0061-\u007a]+", "fox:αλεπού,eagle:αετός"))
print()

x1 = re.search(r"\w+", "♥αβγ!", re.U)
x2 = re.search(r"\w+", "♥αβγ!")

if x1:
    print(x1.group().encode("utf-8"))  # → 「αβγ」
else:
    print("no match")

print(x2, "\n")

d = {"hand": 1, "handy": 2, "handful": 3, "a^b": 4}
words = [re.escape(k) for k in d.keys()]
print(words)
