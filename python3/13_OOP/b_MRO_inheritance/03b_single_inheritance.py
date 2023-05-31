"""
Purpose: Single Inheritance Mechanism

"""


class Base:
    def __init__(self):
        self.__x = 1  # private
        self._y = 2  # protected
        self.z = 3  # public

    def display(self):
        print(f"{self.__x =} {self._y =} {self.z = }")


b = Base()
b.display()  # self.__x =1 self._y =2 self.z = 3
# print(dir(b))

print("b.z", b.z)  # Public
print("b._y", b._y)  # prtet
print("b._Base__x", b._Base__x)


class Derived(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()
        self.__x = 4
        self._y = 5
        self.z = 6


d = Derived()
d.display()  # self.__x =1 self._y =5 self.z = 6


"""
NOTE:
    Private values of Parent/Base/super class cant be modified
    in Child/Derived/sub class
"""
