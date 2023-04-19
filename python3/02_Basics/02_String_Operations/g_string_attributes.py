#!/usr/bin/python3
"""
Purpose: String attributes

Objects
    1. Pen
        -usage: writing, drawing, ....
    2. Mobile
        -usage: communication, messaging, watch videos,
                playing
"""
language = "Python Programming"
print("language       = ", language)
print("type(language) = ", type(language))

print("len(language)  = ", len(language))
print("id(language)   = ", id(language))  # address location

print("===========================================")
print("String Attributes")
print("dir(language) :", dir(language))

# string concatenation
mystr1 = "Taj"
mystr2 = "Mahal"

result = mystr1 + mystr2
print("result = ", result)

result = mystr1.__add__(mystr2)
print("result = ", result)
print()

# string length
print("len(language)     :", len(language))
print("language.__len__():", language.__len__())
print()

# String repetition
result = mystr1 * 5
print("result=", result)

result = mystr1.__mul__(5)
print("result=", result)
print()

print("str(language)     :", str(language))
print("language.__str__():", language.__str__())
print()

print("repr(language)     :", repr(language))
print("language.__repr__():", language.__repr__())
print()

print("language             :", language)
print("language.capitalize():", language.capitalize())
print("language.title()     :", language.title())
print("language.upper()     :", language.upper())
print("language.lower()     :", language.lower())
print("language.swapcase()  :", language.swapcase())
print()

print("'der fluß'.lower()   :", "der fluß".lower())
print("'der fluß'.casefold():", "der fluß".casefold())
print("'der fluss'.lower()  :", "der fluss".lower())
print("'der fluss'.casefold():", "der fluss".casefold())
print()

print("language             :", language)
print("language.istitle()   :", language.istitle())

print('"ABCD123#".isupper() :', "ABCD123#".isupper())
# upper case should be present; lower case absent
print('"Abcd123#".islower() :', "Abcd123#".islower())
print('"abcd123#".islower() :', "abcd123#".islower())
print('"123#".islower()     :', "123#".islower())
print()
# isupper
#     1. atleast one upper case character should present
#     2. lower case character should NOT present

print('"1234".isdigit()     :', "1234".isdigit())
print('"-1234".isdigit()     :', "-1234".isdigit())
print('"1234 ".isdigit()    :', "1234 ".isdigit())
print('"12 34".isdigit()    :', "12 34".isdigit())
print('"123edsd".isdigit()  :', "123edsd".isdigit())
print()

print('"1234".isnumeric()     :', "1234".isnumeric())
print('"-1234".isnumeric()     :', "-1234".isnumeric())
print('"1234 ".isnumeric()    :', "1234 ".isnumeric())
print('"12 34".isnumeric()    :', "12 34".isnumeric())
print('"123edsd".isnumeric()  :', "123edsd".isnumeric())
print()

print('"abcD".isalpha()     :', "abcD".isalpha())
print('"abcd1".isalpha()    :', "abcd1".isalpha())
print()

print('"ab123".isalnum()    :', "ab123".isalnum())
print('"ab123#".isalnum()   :', "ab123#".isalnum())
print('"123".isalnum()      :', "123".isalnum())
print('"abc".isalnum()      :', "abc".isalnum())
print()

print('" ".isspace()        :', " ".isspace())
print('"    ".isspace()     :', "     ".isspace())
print('"    a".isspace()    :', "     a".isspace())
print('"".isspace()         :', "".isspace())
print()

print('ascii("αλεπού")   :', ascii("αλεπού"))
print('ascii("foxfox")   :', ascii("foxfox"))
print('ascii("!@#@#")    :', ascii("!@#@#"))
print()

print('"αλεπού".isascii()    :', "αλεπού".isascii())
print('"foxfox".isascii()    :', "foxfox".isascii())
print('"!@#@#".isascii()    :', "!@#@#".isascii())
print()

print('"ab".isprintable()    :', "ab".isprintable())
print(r'"\n".isprintable()    :', "\n".isprintable())
print(r'"\t".isprintable()    :', "\t".isprintable())
print()

print('"$true".isidentifier() :', "$true".isidentifier())
print('"true".isidentifier() :', "true".isidentifier())
"""
>>> 'name'.isidentifier()
True
>>> 'name123'.isidentifier()
True
>>> 'name_some_1'.isidentifier()
True
>>> 'name_some_TWO'.isidentifier()
True
>>> 'PI'.isidentifier()
True
>>> 'DOZEN'.isidentifier()
True
>>>
>>>
>>> '2name'.isidentifier()
False
>>> '$name'.isidentifier()
False
>>> 'first-name'.isidentifier()
False
>>> ''.isidentifier()
False
>>>
>>>
>>> '_val'.isidentifier()
True
>>> '_-val'.isidentifier()
False
>>> '__val'.isidentifier()
True
>>> '__val__'.isidentifier()
True
>>> '__name__'.isidentifier()
True
>>> '__________name__'.isidentifier()
True
"""
print()

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing

# .find() - to get first occurrence of given substring, within bounds
print('language.find("t")        :', language.find("t"))  # 2

print('language.find("n")        :', language.find("n"))  # 5
print('language.rfind("n")       :', language.rfind("n"))  # 16
print()

print('language.find("n", 6)     :', language.find("n", 6))  # 16
print('language.rfind("n", 15)   :', language.rfind("n", 15))  # 16

print('language.find("n", 6, 17) :', language.find("n", 6, 17))  # 16
print()

print('language.find("Prog")     :', language.find("Prog"))  # 7
print('language.rfind("Prog")    :', language.rfind("Prog"))  # 7
print()

print('language.index("t")       :', language.index("t"))
print('language.index("n")       :', language.index("n"))
print('language.rindex("n")      :', language.rindex("n"))
print()
print('language.index("Prog")    :', language.index("Prog"))
print('language.rindex("Prog")   :', language.rindex("Prog"))
print()

# Question: string attributes - index vs find
# -1 (ITS not REVERSE INDEX)
print('language.find("Q")        :', language.find("Q"))
# print('language.index("Q")       :', language.index('Q')) # ValueError: substring not found


print('language.find("Prog")     :', language.find("Prog"))  # 7
print('language.find("Porg")     :', language.find("Porg"))  # -1
