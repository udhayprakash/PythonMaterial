#!/usr/bin/python
"""
Purpose: Importance of Self

    Self is the placeholder for the instance created
    from that class
"""


class Car:
    Company_name = 'TATA'  # class variable

    def __init__(self, name):
        print('\nNew Car instance is created')
        self.name = name  # instance variable

    def display_name(self):
        return self.name


if __name__ == '__main__':
    tata_nano = Car('tata nano')
    print(tata_nano.display_name())
    print(vars(tata_nano))

    tata_sumo = Car('Tata Sumo')
    print(tata_sumo.display_name())
    print(vars(tata_sumo))
