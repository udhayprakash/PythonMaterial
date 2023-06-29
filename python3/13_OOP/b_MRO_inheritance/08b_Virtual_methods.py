"""
Purpose: Virtual Methods

    virtual method is a method that is declared in a base class and can be overridden by derived classes.
    It allows for polymorphic behavior, which means that the appropriate method implementation is determined
    at runtime based on the actual type of the object.

    Python doesn't have an explicit virtual keyword like some other programming languages.
    By default, all methods in Python are considered to be virtual.
"""


class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement the 'speak' method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()

# Calling the 'speak' method of each object
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
