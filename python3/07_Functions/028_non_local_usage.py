#!/usr/bin/python3
"""
Purpose: non-local usage & inner functions
"""
# Case 0
print('\n\nGeneral case')
name = 'global level'

def outer():
    name = 'outer function level'

    def inner():
        name = 'inner function level'
        print(f'\tIn inner(): {name =}')
    inner()
    print(f'\tIn outer(): {name =}')


outer()
print(f'\toutside   : {name =}')

# Case 1 =========================
print('\n\nwhen global name defined in inner() function')
name = 'global level'


def outer():
    # global name
    name = 'outer function level'

    def inner():
        global name
        name = 'inner function level'
        print(f'\tIn inner(): {name =}')  # changed
    inner()
    print(f'\tIn outer(): {name =}')  # uneffected


outer()
print(f'\toutside   : {name =}')  # effected

# Case 2 =========================
print('\n\nwhen nonlocal name defined in inner() function')
name = 'global level'


def outer():
    name = 'outer function level'

    def inner():
        nonlocal name
        name = 'inner function level'
        print(f'\tIn inner(): {name =}')  # changed
    inner()
    print(f'\tIn outer(): {name =}')  # effected


outer()
print(f'\toutside   : {name =}')  # un-effected

# NOTE:
# 1. If a variable is initialized with global,
#    changes to it with be reflected globally(through out the script),
#    except one-level up.
# 2. If a variable is initialized with "nonlocal",
#    changes to it will be reflected one-level above it

# --Example 2----------------------------------
x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        # global x
        x = 2
        print('inner :', x)

    inner()
    print('outer :', x)
    # not effected when global
    # effected when nonlocal


outer()
print('global:', x)
# effected when global
# not effected when nonlocal
