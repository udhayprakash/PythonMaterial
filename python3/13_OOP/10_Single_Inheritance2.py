#!/usr/bin/python
"""
Purpose: Custom Exception Class
"""


class InvalidAge(Exception):
    def __init__(self, age):
        self.age = age


def validate_age(age):
    if age < 18:
        raise InvalidAge(age)


if __name__ == '__main__':
    age = int(input("please enter your age:"))

    try:
        validate_age(age)
    except Exception as err:
        print("buddy!!! you are still young {}".format(err.age))
    else:
        print("Whom do you want to vote for")

        try:
            voterChoice = int(input('Enter 1. Party1 2. Party2 3. NOTA  :: '))

            vote = {
                1: 'Party1',
                2: 'Party2',
                3: 'NOTA'}
            print('You voted for', vote[voterChoice])
        except Exception as ex:
            print('Invalid Vote')
            print(ex)
