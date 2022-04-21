#!/usr/bin/python3
"""
purpose: regular expression  demo

\d - presence of any digit 0-9
\D - absence of any digit
\w - presence of any alphanumeric a-z A-Z 0-9
\W - absence of any alphanumeric
\s  -presence of  white space AND \n
\S  - absence of white space and \n

\A | Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.
\Z | Matches the expression to its left at the absolute end of a string whether in single or multi-line mode.
\b | Matches the boundary (or empty string) at the start and end of a word, that is, between \w and \W.
\B | Matches where \b does not, that is, the boundary of \w characters.

"""

import re

target_string = '''
Hi everyone!
The PARTY is on 23rd of May 2019, at xyz place. at time 7.30 pm IST
And the RECEPTION is on 30th of Mat, 2019 at xxx place.
Thanks
'''

print(re.findall(r'\w+', target_string))
print(re.findall(r'\W+', target_string))
print()
print(re.findall(r'\s+', target_string))
# ['\n', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', '\n']
print(re.findall(r'\S+', target_string))
# ['Hi', 'everyone!', 'The', 'PARTY', 'is', 'on', '23rd', 'of', 'May', '2019,', 'at', 'xyz', 'place.', 'at', 'time', '7.30', 'pm', 'IST', 'And', 'the', 'RECEPTION', 'is', 'on', '30th', 'of', 'Mat,', '2019', 'at', 'xxx', 'place.', 'Thanks']

'''
>>> re.search('\A123', '123abc')                       # matches '123' placed at the beginning of a string
<_sre.SRE_Match object; span=(0, 3), match='123'>

>>> re.search('bc\Z', '123abc')                            # matches 'bc' placed at the end of a string
<_sre.SRE_Match object; span=(4, 6), match='bc'>

>>> re.search('\\bMy\\b', 'My name is Ethan.')         # matches 'My' placed either at the beginning or end of a string OR placed with word boundaries on either end.
<_sre.SRE_Match object; span=(0, 2), match='My'>

>>> re.search(r'\bMy\b', 'My name is Mythili.')          # matches 'My' placed either at the beginning or end of a string OR placed with word boundaries on either end.
<_sre.SRE_Match object; span=(0, 2), match='My'>

>>> re.search(r'\bEthan\b', 'My name is Ethan.')       # matches 'Ethan' placed either at the beginning or end of a string OR placed with word boundaries on either end. Keep in mind that a period counts as a \W character, and hence it returns a match. A \b character is defined as the boundary between a \w & \W character or between \w and the two ends of a string.
<_sre.SRE_Match object; span=(11, 16), match='Ethan'>

>>> re.search('name\\b', 'My name is Ethan.')          # matches 'name' placed either at the beginning or end of a string OR placed with word boundary on its right side.
<_sre.SRE_Match object; span=(3, 7), match='name'>

>>> re.search('\Bam\B', 'My name is Ethan.')           # matches 'am' surrounded by at least 1 alphanumeric character.
<_sre.SRE_Match object; span=(4, 6), match='am'>

>>> re.search(r'\\', 'x\\y')                           # matches  a single backslash; note that the span component of the match object below suggests a match of only a single backslash
<_sre.SRE_Match object; span=(1, 2), match='\\'>
>>> re.search('\\\\', 'x\\y')                          # matches  a single backslash; note that the span component of the match object below suggests a match of only a single backslash.
<_sre.SRE_Match object; span=(1, 2), match='\\'>


'''
