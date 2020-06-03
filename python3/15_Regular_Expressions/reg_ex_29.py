#!/usr/bin/python
"""
Purpose: lookahead regex

Groups
( ) | Matches the expression inside the parentheses and groups it.

(? ) | Inside parentheses like this, ? acts as an extension notation. Its meaning depends on the character immediately to its right.

(?PAB) | Matches the expression AB, and it can be accessed with the group name.

(?aiLmsux) | Here, a, i, L, m, s, u, and x are flags:

a — Matches ASCII only
i — Ignore case
L — Locale dependent
m — Multi-line
s — Matches all
u — Matches unicode
x — Verbose
(?:A) | Matches the expression as represented by A, but unlike (?PAB), it cannot be retrieved afterwards.

(?#...) | A comment. Contents are for us to read, not for matching.

A(?=B) | Lookahead assertion. This matches the expression A only if it is followed by B.

A(?!B) | Negative lookahead assertion. This matches the expression A only if it is not followed by B.

(?<=B)A | Positive lookbehind assertion. This matches the expression A only if B is immediately to its left. This can only matched fixed length expressions.

(?<!B)A | Negative lookbehind assertion. This matches the expression A only if B is not immediately to its left. This can only matched fixed length expressions.

(?P=name) | Matches the expression matched by an earlier group named “name”.

(...)\1 | The number 1 corresponds to the first group to be matched. If we want to match more instances of the same expresion, simply use its number instead of writing out the whole expression again. We can use from 1 up to 99 such groups and their corresponding numbers.

"""
import re 
result = re.search(r'([A-Za-z]{3})\s(\d{1,2})', 'Feb 5')             
# without ?: syntax; matches 3 letter month, followed by a space, 
# followed by a 1 to 2 digit number.
result.groups()  # ('Feb', '5')


result = re.search(r'(?:[A-Za-z]{3})\s(\d{1,2})', 'Feb 5')
# with ?: syntax; not capturing the month, but using () for precedence and readability.
result.groups()   # ('5',)

## Searching for matches case-insensitively: flags§
# There are 6 six flags that Regular Expressions in Python offer, namely ?iLmsux:

# i: tells the searching engine to ignore case
# L: makes \w, \b, and \s locale dependent
# m: enables multiline expression
# s: the dotall flag; it makes the dot match all characters, including newline character
# u: makes \w, \b, \d, and \s unicode dependent
# x: makes the expression verbose i.e. ignores unescaped whitespace as well as text after # sign i.e. it treats text after # as comments.

# i: tells the searching engine to ignore case
'''
>>> re.search('ETHAN', 'Ethan')                        # does not match
>>> re.search('(?i)ETHAN', 'Ethan')                    # matches
<_sre.SRE_Match object; span=(0, 5), match='Ethan'>  
 
# s: the dotall flag; it makes the dot match all characters, including newline character
>>> re.search('...', 'Hi\n')                       # does not match
>>> re.search('(?s)...', 'Hi\n')                   # matches
<_sre.SRE_Match object; span=(0, 3), match='Hi\n'>
'''

# re.fullmatch()
# The fullmatch(pattern, string, flags=0) performs an anchored search like match(), but returns a match object only if the expression matches the entire string OR the expression matches a portion of string denoted by span indexes specified in optional 2nd and 3rd arguments. Else, it returns None.
'''
>>> pattern = re.compile('ab[cd]')
>>> pattern.fullmatch("zabc")              # doesn't match as 'a' is not at the beginning of "zabc"
>>> pattern.fullmatch("abcde")             # doesn't match as the pattern "ab[cd]" does not match the full string
>>> pattern.fullmatch("abcde", 0, 3)       # matches within specified positions
<_sre.SRE_Match object; span=(0, 3), match='abc'>
'''

'''
>>> re.escape('first.last@domain.com')
'first\\.last\\@domain\\.com'

Once you have gotten the control characters out of the way, you can bring in the special sequences.
>>> pattern = re.compile('(\w+)\\.(\w+)\\@(\w+)\\.(\w+)')
>>> pattern.search('ethan.hunt@mi.com')
<_sre.SRE_Match object; span=(0, 17), match='ethan.hunt@mi.com'>


re.purge() function clears the regular expression caches.
'''




