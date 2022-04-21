#!usr/bin/env python

# Program to illustrate the usage of variable arguments and variable Keyword arguments

# Function to illustrate the behaviour of variable arguments
def test_var_arguments(f_argument, *argv):
    print('first normal arg:', f_argument)
    for arg in argv:
        print('another arg through *argv :', arg)


test_var_arguments('udhay', 'krishna', 'satya', 'Honeywell')

print()


# Function to illustrate the behaviour of variable keyword arguments
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('%s == %s' % (key, value))


greet_me(name='Honeywell')  # Input must be given only in pairs like this
