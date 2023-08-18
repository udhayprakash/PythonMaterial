"""
Purpose: Abstract Classes
    - classes that contain one or more abstract methods.
    - abstract method
        - method that is declared, but contains no implementation.
    - Abstract classes cannot be instantiated, and require subclasses
      to provide implementations for the abstract methods.

"""
from abc import ABC, abstractmethod


# Ordinary classes 1
class OrdinaryClass:
    pass


# Instantiation
o1 = OrdinaryClass()
print(vars(o1))  # {}
print()


# Ordinary classes 2
class OrdinaryClass2:
    def __init__(self, name) -> None:
        self.name = name


# Instantiation
o2 = OrdinaryClass2("Python")
print(vars(o2))  # {'name': 'Python'}
print()


# Ordinary classes 3
class OrdinaryClass:
    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print("Hello world")


# Instantiation
o3 = OrdinaryClass("Python")
print(vars(o3))  # {'name': 'Python'}
o3.say_hello()
print()
print("---------------------------------------------\n\n")


# Abstract Class 1
class AbstractClassExample1(ABC):
    pass


a1 = AbstractClassExample1()
print(a1)
print()


# Abstract Class 2
class AbstractClassExample2(ABC):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()


a2 = AbstractClassExample2("Python")
print(a2)
print()


# Abstract Class 3
class AbstractClassExample3(ABC):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

    def say_hello(self):
        print("Hello world")


# instantiation
a3 = AbstractClassExample3("Python")
print(a3)
a3.say_hello()
print()


# Abstract Class 4
class AbstractClassExample4(ABC):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

    @abstractmethod
    def say_hello(self):
        print("Hello world")


# instantiation
try:
    a4 = AbstractClassExample4("Python")
except TypeError as ex:
    print(ex)


# Can't instantiate abstract class AbstractClassExample4 with abstract method say_hello

# NOTE: If ABC is inherented, we can instatiate; but if one of
# the methods is marked as abstractmethod, we can do even instaiation.


# ----- Real-world Example
class BasicCar(ABC):
    @abstractmethod
    def get_chasis_number(self):
        pass

    def get_car_model(self):
        pass


# Problem
class RolsRoys(BasicCar):
    pass


try:
    car_r = RolsRoys()
except TypeError as ex:
    print(ex)
    print("Excepting methods marked as abstractmethods need to be IMPLEMENTED")


# Solution
class RolsRoys(BasicCar):
    def get_chasis_number(self):
        pass


car_r = RolsRoys()
