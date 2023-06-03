import re

print(re.search("My", "My name is Ethan"))  # <re.Match object; span=(0, 2), match='My'>
print(
    re.search("My", "My name is Mythili")
)  # <re.Match object; span=(0, 2), match='My'>
print(re.findall("My", "My name is Mythili"))  # ['My', 'My']
print()

print(re.findall("\bMy\b", "My name is Mythili"))  # []
print(re.findall(r"\bMy\b", "My name is Mythili"))  #  ['My']
print()

print(re.findall(r"\bMy", "My name is Mythili"))  # ['My', 'My']
print(re.findall(r"\BMy\B", "My name is Mythili"))  # []
print(re.findall(r"My\B", "My name is Mythili"))  # ['My']
print()

print(re.findall(r"\\", "x\\y"))  # ['\\']
print(re.findall(r"\\", r"x\\y"))  # ['\\', '\\']
print()

try:
    re.findall("\\", r"x\\y")
except Exception as ex:
    print(repr(ex))
print()

print(re.findall("\\\\", r"x\\y"))  #  ['\\', '\\']
