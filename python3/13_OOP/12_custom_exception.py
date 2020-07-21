#!/usr/bin/python
"""
Purpose: Custom Exception Class
"""


class InvalidAge(Exception):
    def __init__(self, age):
        self.age = age


def validate_age(_age):
    if _age < 18:
        raise InvalidAge(_age)


if __name__ == '__main__':
    age = int(input('Please Enter Voter Age:'))

    try:
        validate_age(age)
    except Exception as err:
        print("buddy!!! you are still young {}".format(err.age))
    else:
        print('You are eligible for voting')

    # Method Resolution Order
    print(InvalidAge.__mro__)
    # (<class '__main__.InvalidAge'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
    