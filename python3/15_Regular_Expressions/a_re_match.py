#!/usr/bin/python
"""
Purpose: Regular Expressions
"""
import re

# print(dir(re))

target_string = "Python Programming is good for health"
search_string = "Python"

print(f"{target_string.find(search_string) =}")
print(f"{search_string in target_string    =}")
print()

reg_obj = re.compile(search_string)
print(reg_obj, type(reg_obj))

result = reg_obj.match(target_string)
print(f"{result =}")

print(f"result.group():{result.group()}")
print(f"result.span() :{result.span()}")
print(f"result.start():{result.start()}")
print(f"result.end()  :{result.end()}")
