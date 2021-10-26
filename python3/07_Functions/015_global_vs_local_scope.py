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

pi = 3.141  # immutable - call by value


# case 1============
def simple_function():
    print('pi = {}'.format(pi))
    print('pi = {}'.format(pi * 12))
    # print('\nlocals():')
    # pprint(locals())


simple_function()


# case 2 ==================
def simple_function():
    print('before change pi = {}'.format(pi))
    pi = 3333333
    print('after  change pi = {}'.format(pi))
    # print('\nlocals():')
    # pprint(locals())


# simple_function()
# UnboundLocalError: local variable 'pi' referenced before assignment


# case 3=====   call by value
def simple_function(pi):
    print('before change pi    = {}'.format(pi))
    pi = 3333333
    print('after  change pi    = {}'.format(pi))
    print(f'\n{locals()["pi"] = }')
    print(f'\n{globals()["pi"] = }')


simple_function(pi)
print('outside function pi = {}'.format(pi))

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


# case 5=====   call by reference
print()


def simple_function():
    global pi
    print('before change pi    = {}'.format(pi))
    pi = 3333333
    print('after  change pi    = {}'.format(pi))
    # print(f'\n{locals()["pi"] = }')  # KeyError: 'pi'
    print(f'\n{globals()["pi"] = }')


simple_function()
print('outside function pi = {}'.format(pi))
print()
# NOTE:
# 1. For immutable objects, default is call by value.
# 2. When global keyword is used, it will become call by reference.

##############################################
details = {  # mutable - call by reference
    'ver': '3.7.0'
}
# case 6=====   call by reference
print()


def simple_function():
    print(f'\nbefore change ver   = {details["ver"]}')
    details['ver'] = '3.9'
    print(f'After change ver     = {details["ver"]}')
    print(f'\n{globals()["details"] = }')
    print(f'\n{locals().get("details", "no suck key") = }')  # 'no suck key'


simple_function()
print('outside function ver = {}'.format(details['ver']))

# case 7=====   call by reference
print()


def simple_function(lang_details):
    print(f'\nbefore change ver   = {lang_details["ver"]}')
    details['ver'] = '3.10'
    print(f'After change ver    = {lang_details["ver"]}')
    print(f'\n{id(globals()["details"])}{ globals()["details"]    = }')  # {'ver': '3.10'}
    print(f'\n{id(locals()["lang_details"])} {locals()["lang_details"]= }')  # {'ver': '3.10'}


simple_function(details)
print('outside function ver = {}'.format(details['ver']))

# case 8=====   call by reference
print()


def simple_function(lang_details):
    lang_details2 = lang_details.copy()
    print(f'\nbefore change ver   = {lang_details2["ver"]}')
    details['ver'] = '3.11'
    print(f'After change ver    = {lang_details2["ver"]}')
    print(f'\n{id(globals()["details"])}{ globals()["details"]    = }')  # {'ver': '3.10'}
    print(f'\n{id(locals()["lang_details2"])} {locals()["lang_details2"]= }')  # {'ver': '3.10'}


simple_function(details)
print('outside function ver = {}'.format(details['ver']))

# case 8=====   call by reference
print()
my_list = [1, 2, 3]


def simple_function():
    print(f'\nbefore change my_list   = {my_list}')
    my_list.append(4)
    print(f'After change my_list     = {my_list}')


simple_function()
print('outside function new_list = {}'.format(my_list))

# case 9=====   call by reference
print()
my_list = [1, 2, 3]


def simple_function(my_list):
    print(f'\nbefore change my_list = {my_list}')
    my_list.append(5)
    print(f'After change my_list = {my_list}')


simple_function(my_list)
print('outside function new_list = {}'.format(my_list))

# case 10=====   call by value
print()
new_list = [1, 2, 3]


def simple_function(new_list):
    print(f'\nbefore change new_list = {new_list}')
    new_list += [6]
    print(f'After change new_list = {new_list}')


simple_function(new_list)
print('outside function new_list = {}'.format(new_list))
