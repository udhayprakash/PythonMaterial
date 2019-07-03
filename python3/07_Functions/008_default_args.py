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
 
def myfunc(var1, var2, var3=0):
    """
    Function to perform arithmetic Multiplication operation
    :param num1: Number
    :param num2: Number
    :return: result of addition operation
    """
    return var1 + var2 + var3


print('myfunc(2, 3, 5)=', myfunc(2, 3, 5))
print('myfunc(2, 3)   =', myfunc(2, 3))


def hello_world(name):
    print('Hello ' + name)

# hello_world() # TypeError: hello_world() missing 1 required positional argument: 'name'
hello_world('chaitra')


def hello_world(name= 'world'):
    print('Hello ' + name)

hello_world()
hello_world('chaitra')



def person_details(name='alpha', age=99):
    print('{} with age {}'.format(name, age))

person_details()
person_details('chaitra')
person_details('chaitra', 20)

# NOTE: default arguments should be at the end

def person_details_2(designation, name='alpha', age=99):
    print(designation + ' {} with age {}'.format(name, age))

# person_details_2() # TypeError: person_details_2() missing 1 required positional argument: 'designation'
person_details_2('developer')
person_details_2('tester', 'chaitra')
person_details_2('tester', 'chaitra', 45)


person_details_2(designation='tester', name='chaitra', age=5)


# # Function Definition
# def hello(height, name='BINDU',age=200):
#     # print "%s's age is %d with height %d"%(name, age, height)
#     print("{0}'s age is {1} with height {2}".format(name, age, height))

# # NOTE: default arguments should be at the end

# # Function Call 
# # hello()
# hello(1)  # mandatory args shoud be given

# # # hello('HARI')
# # # hello(1, 'HARI')

# # # hello('Python')
# # # hello(1,365)

# # hello(1,'India', 75)
