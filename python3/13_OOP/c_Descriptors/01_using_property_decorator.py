"""
Purpose: property Decorator

- USECASE: Helps in controlling life-cycle of variable
"""
import logging

logging.basicConfig(level=logging.DEBUG)


class subject:
    count = 0

    def __init__(self, name):
        self.name = name  # Public Variable
        self.dozen = 12

    @property  # .getter
    def name(self):  # retrieving
        logging.debug("get method is called")
        return self._name

    @name.setter
    def name(self, name):  # creation, Updating
        logging.debug("set method is called")
        self._name = name  # Protected variable

    @name.deleter
    def name(self):  # deleting
        logging.debug("deleter method is called")
        del self._name

    # name = property(get_value, set_value, del_value)


s = subject("udhay")
print()

print(f"{s.name = }")
print()

s.name = "Prakash"
print(f"{s.name = }")
print()

print(vars(s))
print(f"{s._name = }")
# NOTE: These methods wont be called if we are accessing the Protected variables

print("===========================")
del s.name
print(vars(s))
try:
    s.name
except AttributeError as ex:
    print(ex)

print("===========================")

print(f"{s.dozen = }")
# NOTE: property is associated with 'name' instance variable ONLY
