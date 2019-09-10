#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

language = 'Python Programming'
print('language       = ', language)
print('type(language) = ', type(language))
print('id(language)   = ', id(language))
print('===========================================')
print('String Attributes')
print('dir(language) :', dir(language))

# string concatenation
mystr1 = 'Taj'
mystr2 = "Mahal"

result = mystr1 + mystr2
print('result=', result)

result = mystr1.__add__(mystr2)
print('result=', result)
print()

print('len(language)     :', len(language))
print('language.__len__():', language.__len__())
print()

result = mystr1 * 4
print('result=', result)

result = mystr1.__mul__(4)
print('result=', result)
print()

print('str(language)     :', str(language))
print('language.__str__():', language.__str__())
print()

print('repr(language)     :', repr(language))
print('language.__repr__():', language.__repr__())
print()

print(language)
print('language.capitalize():', language.capitalize())
print('language.title()     :', language.title())
print('language.upper()     :', language.upper())
print('language.lower()     :', language.lower())
print('language.swapcase()  :', language.swapcase())
print()
print(language)

print('language.istitle()   :', language.istitle())

print('"ABCD123#".isupper() :', "ABCD123#".isupper())
print('"Abcd123#".islower() :', "Abcd123#".islower())

print('"1234".isdigit()     :', "1234".isdigit())
print('"123edsd".isdigit()  :', "123edsd".isdigit())

print('"abcD".isalpha()     :', "abcD".isalpha())
print('"abcd1".isalpha()    :', "abcd1".isalpha())

print('"ab123".isalnum()    :', "ab123".isalnum())
print('"ab123#".isalnum()   :', "ab123#".isalnum())

print('" ".isspace()        :', " ".isspace())
print('"".isspace()         :', "".isspace())
print()

# # P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# # 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17   - forward indexing


# print('language.find("t")    :', language.find('t'))   # 2
# print('language.find("n")    :', language.find('n'))   # 5
# print('language.rfind("n")   :', language.rfind('n'))  #16
# print()
# print('language.find("Prog")   :', language.find('Prog'))   # 7
# print('language.rfind("Prog")  :', language.rfind('Prog'))  # 7
# print()
# print('language.index("t")       :', language.index('t'))
# print('language.index("n")       :', language.index('n'))
# print('language.rindex("n")      :', language.rindex('n'))
# print()
# print('language.index("Prog")    :', language.index('Prog'))
# print('language.rindex("Prog")   :', language.rindex('Prog'))

# #string attributes - index vs find
# print('language.find("Q")   :', language.find('Q'))     # -1
# # print('language.index("Q")   :', language.index('Q'))  # ValueError
