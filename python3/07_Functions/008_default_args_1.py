#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with default arguments
"""

  
# def myfunc(num1, num2):
#     """
#     Function to perform arithmetic Addition operation
#     :param num1: Number
#     :param num2: Number
#     :return: result of addition operation
#     """
#     return num1 + num2
 
def myfunc( var1, var2, var3=0):
    """
    Function to perform arithmetic Multiplication operation
    :param num1: Number
    :param num2: Number
    :return: result of addition operation
    """
    return var1 + var2 + var3


print('myfunc(2, 3, 5)=', myfunc(2, 3, 5))
print('myfunc(2, 3)   =', myfunc(2, 3))


# def hello_world(name):
#     print('Hello ' + name)

# # hello_world() # TypeError: hello_world() missing 1 required positional argument: 'name'
# hello_world('chaitra')


def hello_world(name= 'world'):
    print('Hello ' + name)

hello_world()
hello_world('chaitra')
hello_world(name='chaitra')


############################################
def person_details(name='alpha', age=99):
    print('{} with age {}'.format(name, age))

person_details()
person_details('chaitra')
person_details(20)
person_details('chaitra', 20)
print()
person_details(name='chaitra')
person_details(age=20)

# NOTE: default arguments should be at the end

def person_details_2(designation, name='alpha', age=99):
    # print(designation + ' {} with age {}'.format(name, age))
    print(f'{name} with age {age}')

# person_details_2() # TypeError: person_details_2() missing 1 required positional argument: 'designation'
person_details_2('developer')
person_details_2('tester', 'chaitra')
person_details_2('tester', 'chaitra', 45)

# person_details_2(name='developer')
person_details_2(designation='tester', name='chaitra', age=5)

