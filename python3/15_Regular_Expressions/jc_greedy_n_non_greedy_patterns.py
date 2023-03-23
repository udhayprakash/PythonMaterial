#!/usr/bin/python3
"""
Purpose: Regular Expressions

    Greedy Patterns
     .+  Any character( except newline) can occur  1 or any no. of time
     .*  Any character( except newline) can occur  0 or any no. of time

"""
import re

res = re.search("a.*", "a")
if res:
    res.group()

print(re.search("a.*", "a").group())  # b is occurring 0 times
print(re.search("a.*", "ab").group())  # b is occurring 1 times
print(re.search("a.*", "abb").group())  # b is occurring 2 times
print(re.search("a.*", "abbb").group())  # b is occurring 3 times
print(re.search("a.*", "abbbc").group())  # b is occurring 3 times
print()

# print(re.search('a.*', 'bbbbbbb').group())     # a is occurring 0 times
print(re.search("a*.*", "bbbbbbb").group())  # a is occurring 0 times
print()

# Question
print(re.search(".*", "").group())  # '' - empty string is resulted
print(re.search(".*", "aS").group())
print(re.search(".*", "ASDASDSADS").group())
print(re.search(".*", "ASDASDSADS 3444 *&(*&(_)_.dfaderrrerq").group())
print(re.search(".*", "ASDASDSADS 34\n44 *&(*&(_)_.dfaderrrerq").group())
print()

# ------------
print(re.search(".*", "").group())  # any char occurred 0 times
# print(re.search(".+", "").group())  # any char occurred 0 times

print(re.search(".+", "c").group())  # any char occurred 1 times

print("Non-Greedy Pattern")
print(re.search(".?", "").group())  # any char occurred 1 times
print(re.search(".?", "c").group())  # any char occurred 1 times
print()
print(re.search(".*", "ccccccc").group())  # any char occurred 7 times
print(re.search(".+", "ccccccc").group())  # any char occurred 7 times
print(
    re.search(".?", "ccccccc").group()
)  # any char occurred 7 times; only 1 time taken
print()

# ----------------
print(re.search("", "<h1>name</h1>").group())
print(re.search("<h1>", "<h1>name</h1>").group())  # <h1>
print(re.search("<..>", "<h1>name</h1>").group())  # <h1>
print()

# greedy pattern
print(re.search("<.+>", "<h1>name</h1>").group())  # <h1>name</h1>
print(re.search("<.*>", "<h1>name</h1>").group())  # <h1>name</h1>

# non greedy pattern
print(re.search("<.+?>", "<h1>name</h1>").group())  # <h1>
print(re.search("<.*?>", "<h1>name</h1>").group())  # <h1>
print()

print(re.search(r"\d", "150").group())  # 1
print(re.search(r"\d*", "150").group())  # 150
print(re.search(r"\d+", "150").group())  # 150
print(re.search(r"\d?", "150").group())  # 1

print(re.search(r"\d", "cost of apples is $150 per basket").group())  # 1
print(re.search(r"\d*", "cost of apples is $150 per basket").group())  # 150
print(re.search(r"\d+", "cost of apples is $150 per basket").group())  # 150
print(re.search(r"\d?", "cost of apples is $150 per basket").group())  # 1
