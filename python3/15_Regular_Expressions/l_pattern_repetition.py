#!/usr/bin/python3
"""
Purpose: Regular Expressions

Pattern repetition
    {}  specifies the number of times, the previous character should present

Mid-way between greedy and non-greedy patterns
"""

import re

print(re.findall("ab{0}", "a ab abb abbbb abbbbbbb abbbbbbbbbb"))
print(re.findall("ab{2}", "a ab abb abbbb abbbbbbb abbbbbbbbbb"))
print(re.findall("ab{5}", "a ab abb abbbb abbbbbbb abbbbbbbbbb"))

# range of repetition
print(re.findall("ab{2,5}", "a ab abb abbbb abbbbbbb abbbbbbbbbb"))
print("-----------")


print(re.match("a{1,2}?shique", "aashique").group())
print(re.search("a{1,2}?shique", "aashique").group())

print(re.match("a{1,2}?shique", "ashique").group())
print(re.search("a{1,2}?shique", "ashique").group())

print(re.search("a{1,2}?shique", "aaaaashique").group())

print(re.search("a{1,2}?", "aaaaa").group())
print(re.search("a{1,2}", "aaaaa").group())

print("-----------")

print(re.match(r"(..)*", "alb2cs").group(1))
print(re.match(r"(..)+", "alb2cs").group(1))
print(re.match(r"(..)?", "alb2cs").group(1))
