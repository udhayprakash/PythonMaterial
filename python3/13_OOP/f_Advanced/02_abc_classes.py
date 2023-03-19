#!/usr/bin/python
"""
Purpose: Abstract Base classes

"""
from abc import ABC, abstractmethod, abstractproperty


class BasicCar(ABC):
    modal_name: str = NotImplemented

    @abstractmethod
    def get_chasis_number(self):
        pass

    def get_car_model(self):
        pass


# Solution
class RolsRoys(BasicCar):
    def get_chasis_number(self):
        pass


car_r = RolsRoys()


# NOTE: We cant enforce variables to be defined.
# for that we need to use property
# ----------------------------------------
class BasicCar(ABC):
    @abstractmethod
    def get_chasis_number(self):
        pass

    def get_car_model(self):
        pass

    @property
    @abstractmethod
    def modal_name(self):
        pass


# NOTE: Earlier asbtractproperty is used, but deprecated in Python 3.8
# Solution
class RolsRoys(BasicCar):
    def get_chasis_number(self):
        pass

    @property
    def modal_name(self):
        pass


car_r = RolsRoys()
