#!/usr/bin/python3
"""
Purpose: string attributes
"""

# str.strip()


print("  python Production  ")
print()
print("  python Production  ".strip())
print("  python Production  ".strip("p"))
print("  python Production  ".strip("p "))
print("  python Production  ".strip("p thno"))
print("  python Production  ".strip("p thnoy"))  # 'Producti'

# >>> "  python Production  ".strip(" ").strip("pn").strip("t").strip("i").strip("o").strip("y")
# 'thon Producti'

# >>> "  python Production  ".strip(" pntioy")
# 'hon Produc'

"aaaaaaaaaaaaaaaaaaaaaa".strip("a")  # ''
"aaaaaaaa b aaaaaaaaaaa".strip("ab")  # ' b '
"aaaaaaaa b aaaaaaaaaaa".strip("ab ")  # ''

print()
print("  python Production  ".strip())
print("  python Production  ".lstrip())
print("  python Production  ".rstrip())
print("  python Production  ".lstrip("p thnoy"))
print("  python Production  ".rstrip("p thnoy"))

print("00001231231230".lstrip("0"))
"123".zfill(3)  # '123'
"123".zfill(4)  # '0123'
"123".zfill(7)  # '0000123'
"0" * 4 + "123"  # '0000123'


# How to convert a string to a list
print("Python Production".split())  # ['Python', 'Production']
print("Python Production".split(" "))  # ['Python', 'Production']
print("Python Production".split("r"))  # ['Python P', 'oduction']
print("Python Production".split("t"))  # ['Py', 'hon Produc', 'ion']
print()

# Question: what is the type of result, if splitting substring is not present
print("Python Production".split("p"))  # ['Python Production']
print("Python Production".split("P"))  # ['', 'ython ', 'roduction']
print("Python Production".split("n"))  # ['Pytho', ' Productio', '']

print("Python Production".split("Prod"))  # ['Python ', 'uction']
print("Python Production".split("Prdo"))  # ['Python Production']

# print('Python Production'.split('')) # ValueError: empty separator

# Question:
"".split()  # []
" ".split()  # []
" ".split(" ")  # ['', '']
"".split(" ")  # ['']

print()
print("1201201301201".split("0"))  # ['12', '12', '13', '12', '1']
print("1201201301201".split("0", maxsplit=0))  # ['1201201301201']
print("1201201301201".split("0", maxsplit=1))  # ['12', '1201301201']
print("1201201301201".rsplit("0", maxsplit=1))  # ['12012013012', '1']

print("1201201301201".split("0", 3))  # ['12', '12', '13', '1201']
print("1201201301201".rsplit("0", 3))  # ['12012', '13', '12', '1']
print()

# Question:
"1,2,3".split(",")  # ['1', '2', '3']
"1,2,,3,".split(",")  # ['1', '2', '', '3', '']

# default is with white space
"1 2 3".split()  # ['1', '2', '3']
"   1   2  3   ".split()  # ['1', '2', '3']
"   1   2  3   ".split(" ")  # ['', '', '', '1', '', '', '2', '', '3', '', '','']

print()

# partition - will result in 3 values in tuple
print("Python Production".split("r"))  # ['Python P', 'oduction']
print("Python Production".partition("r"))  # ('Python P', 'r', 'oduction')

print("Python Production".split("d"))  # ['Python Pro', 'uction']
print("Python Production".partition("d"))  # ('Python Pro', 'd', 'uction')

"Python Production".split("t")  # ['Py', 'hon Produc', 'ion']
"Python Production".partition("t")  # ('Py', 't', 'hon Production')
"Python Production".rpartition("t")  # ('Python Produc', 't', 'ion')

# How to convert a string to a list
print(
    list("1201201301201")
)  # ['1', '2', '0', '1', '2', '0', '1', '3', '0', '1', '2', '0', '1']

print(
    tuple("1201201301201")
)  # ('1', '2', '0', '1', '2', '0', '1', '3', '0', '1', '2', '0', '1')
print(set("1201201301201"))  # {'2', '1', '0', '3'}
print()


# Question: How to convert list of strings to a single string
print("Python" + "Production" + "Language")  # PythonProductionLanguage
print("Python" + " " + "Production" + " " + "Language")  # Python Production Language
print("Python" + "-" + "Production" + "-" + "Language")  # Python-Production-Language

# ''.join('Python', 'Production', 'Language')
# TypeError: join() takes exactly one argument (3 given)
print()
print("".join(["Python", "Production", "Language"]))  # PythonProductionLanguage
print(" ".join(["Python", "Production", "Language"]))  # Python Production Language
print("-".join(["Python", "Production", "Language"]))  # Python-Production-Language
print("@".join(["Python", "Production", "Language"]))  # Python@Production@Language

print("0".join(["1", "2", "3", "4", "5"]))  # '102030405'
# print('0'.join(['1', '2', '3', '4', 5]))
# TypeError: sequence item 4: expected str instance, int found

# print('0'.join([1, 2, 3, 4, 5]))
# TypeError: sequence item 0: expected str instance, int found

print()
print("___".join("Python Production".split("P")))  # ___ython ___roduction
print("P".join("Python Production".split("P")))  # Python Production
print("R".join("Python Production".split("P")))  # Rython Rroduction
print()

print("Python Production".replace("P", "R"))  # Rython Rroduction
print("Python Production".replace("Prod", "cat"))  # Python catuction
print("Python Production".replace("Prod1", "cat"))  # Python Production

"aaaaaaaaaaa".replace("a", "b")  # 'bbbbbbbbbbb'
"aaaaaaaaaaa".replace("a", "b", 2)  # 'bbaaaaaaaaa'
# Asssignment: Check how to replace from right to left
