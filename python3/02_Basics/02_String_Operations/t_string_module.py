#!/usr/bin/python3
"""
Purpose: String Module
"""
import string

# print(dir(string))
print(string.__doc__, end="\n\n")

print(f"{string.ascii_letters   =}")
print(f"{string.ascii_lowercase =}")
print(f"{string.ascii_uppercase =}")
print(f"{string.digits          =}")
print(f"{string.hexdigits       =}")
print(f"{string.octdigits       =}")
print(f"{string.printable       =}")
print(f"{string.punctuation     =}")
print(f"{string.whitespace      =}")
print()

print(f'{string.capwords("aaaaaaaaaaaaaaaaa")=}')
print(f'{string.capwords("11111111111111111")=}')
print(f'{string.capwords("one two three 345")=}')  # str.title
print()

s = "let us capitalize every word of this sentence."
print(string.capwords(s))
print(s.title())


t = string.Template("Hello $name!")
t.substitute(name="World")  # 'Hello World!'

t = string.Template("""name: $name - $$name - $$$name  age : ${age}years""")
# t.substitute(name='World')  # KeyError: 'age'
t.substitute(name="World", age=30)  # 'name: World - $name - $World  age : 30years'

# NOTE: $$ is an escape; it is replaced with a single $.
# ${identifier} is equivalent to $identifier

string.Template("$who likes $what").substitute({"who": "udhay", "what": "python"})
# 'udhay likes python'

string.Template("$who likes $what").substitute({"who": "udhay"})
# KeyError: 'what'

string.Template("$who likes $what").safe_substitute({"who": "udhay"})
# 'udhay likes $what'
