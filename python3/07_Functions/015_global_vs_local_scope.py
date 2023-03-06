#!/usr/bin/python3
"""
Purpose: Functions

   Scope - Global and local

call by value
    - changes within the function will NOT reflect at the global level

call by reference
    - changes within the function will reflect at the global level

immutable objects - int, float, None, bool, tuple, string, frozenset
mutable objects   - list, set, dict, bytearray string

NOTE:
-----
mutable object can be edited within function without passing as args
immutable object CANT be edited within function without passing as args
"""
# print('\nglobals():')
# pprint(globals())
#
# print('\nlocals():')
# pprint(locals())
#
# assert globals() == locals()

from audioop import reverse

print("\n case 1============")
pi = 3.141  # immutable - call by value


def simple_function():
    print("pi = {}".format(pi))
    print("pi = {}".format(pi * 12))
    # print('\nlocals():')
    # pprint(locals())


simple_function()


print("\n case 2 ==================")


def simple_function():
    print("before change pi = {}".format(pi))
    pi = 3333333
    print("after  change pi = {}".format(pi))
    # print('\nlocals():')
    # pprint(locals())


# simple_function()
# UnboundLocalError: local variable 'pi' referenced before assignment

print("\n case 3=====   call by value")


def simple_function(pi):
    print("before change pi    = {}".format(pi))
    pi = 3333333
    print("after  change pi    = {}".format(pi))
    print(f'\n{locals()["pi"] = }')
    print(f'\n{globals()["pi"] = }')


simple_function(pi)
print("outside function pi = {}".format(pi))

# NOTE: changes with in function are not reflected outside it.
# -- This is called as CALL BY VALUE


# # case 4=====   call by reference
# def simple_function(pi):
#     global pi
#     print('before change pi = {}'.format(pi))
#     pi = 3333333
#     print('after  change pi = {}'.format(pi))

# simple_function(pi) # SyntaxError: name 'pi' is parameter and global
# print('outside function pi = {}'.format(pi))

print("\n case 5=====   call by reference")


def simple_function():
    global pi
    print("before change pi    = {}".format(pi))
    pi = 3333333
    print("after  change pi    = {}".format(pi))
    # print(f'\n{locals()["pi"] = }')  # KeyError: 'pi'
    print(f'\n{globals()["pi"] = }')


simple_function()
print("outside function pi = {}".format(pi))
print()
# NOTE:
# 1. For immutable objects, default is call by value.
# 2. When global keyword is used, it will become call by reference.

##############################################
print("\n case 6=====   call by reference")
details = {"ver": "3.7.0"}  # mutable - call by reference


def simple_function():
    print(f'\nbefore change ver   = {details["ver"]}')
    details["ver"] = "3.9"
    print(f'After change ver     = {details["ver"]}')
    print(f'\n{globals()["details"] = }')
    print(f'\n{locals().get("details", "no suck key") = }')  # 'no suck key'


simple_function()
print("outside function ver = {}".format(details["ver"]))

print("\n case 7=====   call by reference")


def simple_function(lang_details):
    print(f'\nbefore change ver   = {lang_details["ver"]}')
    details["ver"] = "3.10"
    print(f'After change ver    = {lang_details["ver"]}')
    # {'ver': '3.10'}
    print(f'\n{id(globals()["details"])}{ globals()["details"]    = }')
    # {'ver': '3.10'}
    print(f'\n{id(locals()["lang_details"])} {locals()["lang_details"]= }')


simple_function(details)
print("outside function ver = {}".format(details["ver"]))

print("\n case 8=====   call by reference")


def simple_function(lang_details):
    lang_details2 = lang_details.copy()
    print(f'\nbefore change ver   = {lang_details2["ver"]}')
    details["ver"] = "3.11"
    print(f'After change ver    = {lang_details2["ver"]}')
    # {'ver': '3.10'}
    print(f'\n{id(globals()["details"])}{ globals()["details"]    = }')
    # {'ver': '3.10'}
    print(f'\n{id(locals()["lang_details2"])} {locals()["lang_details2"]= }')


simple_function(details)
print("outside function ver = {}".format(details["ver"]))

print("\n case 8=====   call by reference")
my_list = [1, 2, 3]


def simple_function():
    print(f"\nbefore change my_list   = {my_list}")
    my_list.append(4)
    print(f"After change my_list     = {my_list}")


simple_function()
print("outside function new_list = {}".format(my_list))

print("\n case 9=====   call by reference")
my_list = [1, 2, 3]


def simple_function(my_list):
    print(f"\nbefore change my_list = {my_list}")
    my_list.append(5)
    print(f"After change my_list = {my_list}")


simple_function(my_list)
print("outside function new_list = {}".format(my_list))

print("\n case 10=====   call by Reference - for Global Mutable objects")


def simple_function(new_list):
    print(f"\nbefore change new_list = {new_list}")  # [1, 2, 3]
    new_list += [6]
    print(f"After change new_list = {new_list}")  # [1, 2, 3, 6]


new_list = [1, 2, 3]
simple_function(new_list)
print("outside function new_list = {}".format(new_list))  # [1, 2, 3, 6]


print("\n case 11=====   call by Reference - for Global Mutable objects")


def add_N_to_list(_new_list, n):
    print(f"\nbefore change new_list = {_new_list}")  # [1, 2, 3]
    _new_list[:] = [num + n for num in _new_list]
    print(f"After change new_list = {_new_list}")  # [6, 7, 8]


new_list = [1, 2, 3]
add_N_to_list(new_list, 5)
print("outside function new_list = {}".format(new_list))  # [6, 7, 8]


print("\n\n # LEAKAGE ISSUE")


def simple_function(mylist2):
    # [1, 2, 3]
    print(f"\nbefore change mylist2 = {mylist2} {id(mylist2)}")
    mylist2.sort(reverse=True)
    # [1, 2, 3, 6]
    print(f"After change mylist2 = {mylist2} {id(mylist2)}")


new_list = [1, 2, 3]
simple_function(new_list)

print(f"outside function new_list = {new_list} {id(new_list)}")  # [1, 2, 3, 6]


def simple_function(mylist2):
    print(f"\nbefore change mylist2 = {mylist2} {id(mylist2)}")  # [1, 2, 3]
    mylist2 = sorted(mylist2, reverse=True)
    print(f"After change mylist2 = {mylist2} {id(mylist2)}")  # [1, 2, 3, 6]


new_list = [1, 2, 3]
simple_function(new_list)
print(f"outside function new_list = {new_list} {id(new_list)}")  # [1, 2, 3, 6]

# NOTE:
# immuatble -- by dfault cal by value; with global, call by ReferenceError
# mutable -- by dfault is call by refernece; create copy() to call by value
