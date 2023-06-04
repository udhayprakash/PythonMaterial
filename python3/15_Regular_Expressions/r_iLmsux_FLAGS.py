"""
Purpose: Regular Expressions flags ?iLmsux
    i: tells the searching engine to ignore case
    L: makes \w, \b, and \s locale dependent
    m: enables multiline expression
    s: the dotall flag; it makes the dot match all characters, including newline character
    u: makes \w, \b, \d, and \s unicode dependent
    x: makes the expression verbose i.e. ignores unescaped whitespace as well as text after # sign i.e. it treats text after # as comments.
"""
import re

print("\n(?i)")
print(re.findall("hello", "Hello World", flags=re.IGNORECASE))
print(re.findall("(?i)hello", "Hello World"))
print()

print("\n(?s)")
print(re.search("...", "Hi\n"))  # does not match
print(re.search("(?s)...", "Hi\n"))  # matches
print()

# ------------------------------------------------
print("\n(?m)")

text = """
Line 1
Line 2
Line 3
"""
print(re.findall("^Line \d+$", text, flags=re.MULTILINE))
print(re.findall("(?m)^Line \d+$", text))
print()
