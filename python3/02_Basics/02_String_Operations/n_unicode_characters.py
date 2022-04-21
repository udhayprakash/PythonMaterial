#!/usr/bin/python3
"""
Purpose: unicode characters

ASCII - english characters & commonly used symbols
      - 0 to 127

      65 - A
      66 - B
      67 - C
      .....
      97 - a
      98 - b
      99 - c
 Further Reference: https://home.unicode.org/
"""
# chr() & ord()

import sys

print(f"{ord('A') =}")  # 65
print(f"{ord('B') =}")  # 66
print(f"{ord('C') =}")  # 67
print()

print(f"{ord('a') =}")  # 97
print(f"{ord('b') =}")  # 98
print(f"{ord('c') =}")  # 99
print()

print(f"{ord('1') =}")  # 49
print(f"{ord('2') =}")  # 50
print(f"{ord('3') =}")  # 51
print()

print(f"{ord('$') =}")  # 36
print(f"{chr(36)  =}")  # '$'

# print(f"{ord('ap') =}")
# TypeError: ord() expected a character, but string of
# length 2 found

print(f"{chr(0)    =}")  # '\x00'
print(f"{chr(127)  =}")  # '\x7f'
print()

# > 127 ---> unicode characters
print(f"{chr(129)  =}")  # '\x81'

# \uXXX - unicode character
print("\u20B9")  # ₹
print("\u018e")  # Ǝ
print("noe\u0308l")  # noël
print()

print("\046")
# \x... - hexadecimal number
print("\x24")
print("\xf1")
print()

# One-character Unicode strings can also be created with the chr() built-in function
print(chr(57344))  # '\ue000'
print(ord("\ue000"))  # 57344

for i in range(0, 128):
    print(i, chr(i))
print()

for i in range(3000, 3500):
    print(i, chr(i))

print(f"{sys.maxunicode =}")

# string reversal on unicode characters is tricky
s6 = "noe\u0308l"
print(s6)  # 'noël'
print("".join(reversed(s6)))  # 'l̈eon'
print(s6[::-1])  # 'l̈eon'
