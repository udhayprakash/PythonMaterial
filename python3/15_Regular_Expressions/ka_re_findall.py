"""
Purpose: Regular Expressions

    .  any character, except newline
    \d - presence of any digit 0-9
    \D - absence of any digit

    \w - presence of any alphanumeric a-z A-Z 0-9
    \W - absence of any alphanumeric a-z A-Z 0-9

    \s  -presence of  white space AND \n
    \S  - absence of white space and \n

    \A | Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.
    \Z | Matches the expression to its left at the absolute end of a string whether in single or multi-line mode.

    \b | Matches the boundary (or empty string) at the start and end of a word, that is, between \w and \W.
    \B | Matches where \b does not, that is, the boundary of \w characters.

"""

import re

# re.match() -> to get a pattern at first of search string
# re.search() -> to get a pattern at any place in search string

# re.findall() -> to get all the patterns within the search string

print(re.match("python", "PYTHON python PYTHon pYTHon43454", re.I).group())
print(re.search("python", "PYTHON python PYTHon pYTHon43454", re.I).group())
print()

print(re.findall("python", "PYTHON python PYTHon pYTHon43454"))
print(re.findall("python", "PYTHON python PYTHon pYTHon43454", re.I))
print()

target_string = """
Hi everyone!
The PARTY is on 23rd of May 2020, at xyz place. at time 7.30 pm IST
And the RECEPTION is on 30th of May, 2020 at xxx place.
Thanks
"""
print(re.findall("2", target_string, re.I))
print(re.findall("2020", target_string, re.I))
print()

print(re.findall(r"\d", target_string))
# print(re.findall(r'\d*', target_string))
print(re.findall(r"\d+", target_string))
print()

print(re.findall("[0-9]", target_string))
print(re.findall("[0-9]+", target_string))
print()

print(re.findall("[1-5]", target_string))
print(re.findall("[1-5]+", target_string))
print(re.findall("[357]+", target_string))
print()

print(re.findall(r"\w", target_string))
print(re.findall(r"\w+", target_string))
print()

print(re.findall("[a-zA-Z0-9]", target_string))
print(re.findall("[a-zA-Z0-9]+", target_string))
print()

print(re.findall("[a-z]", target_string))
print(re.findall("[a-z]+", target_string))
print()

print(re.findall("[aeiou]", target_string, re.I))
print(re.findall("[a-zA-Z]+", target_string))
print()


print(re.findall(r"\s+", target_string))
print(re.findall(r"\S+", target_string))
print()


print(re.findall(r"\w+", target_string))
print(re.findall(r"\W+", target_string))
