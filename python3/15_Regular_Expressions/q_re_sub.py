"""
Purpose: re.sub and re.subn

"""

import re

p = re.compile("(blue|white|red)")
print(p.match("blue Lorries and red Busses").group())
print(p.search("blue Lorries and red Busses").group())
print(p.findall("blue Lorries and red Busses"))
print()

print(p.sub("colour", "blue Lorries and red Busses"))
print(p.subn("colour", "blue Lorries and red Busses"))
print(p.subn("colour", "blue Lorries and red Busses", count=1))
print()

print(re.sub(r"(apple|banana|orange)", "fruit", "apple, banana, orange"))
print()

print("\n Replacing with backreference")
print(re.sub(r"(SIX|SEVEN)", lambda res: res.group(1) + "teen", "FIVE,SIX,SEVEN,EIGHT"))
print(re.sub(r"(SIX|SEVEN)", r"\1teen", "FIVE,SIX,SEVEN,EIGHT"))
print()

# --------------------------------------------
counter = 1


def repl(match):
    global counter
    result = f"({counter}) {match.group(0)}"
    counter += 1
    return result


new_text, count = re.subn(r"\b\w+\b", repl, "Hello, World! Goodbye, World!")
print(f"{new_text =}")
print("Number of replacements:", count)
