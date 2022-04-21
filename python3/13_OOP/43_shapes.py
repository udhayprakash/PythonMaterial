# Write class(es) that represent the following shapes:
#       square, rectangle, circle.
# Each shape should have a perimeter and an area.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, length, bredth=None):
        self.length = length
        self.bredth = bredth
        super().__init__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class circle(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return math.pi * (self.length**2)

    def perimeter(self):
        return 2 * math.pi * self.length


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length**2

    def perimeter(self):
        return self.length * 2


class Rectangle(Shape):
    def __init__(self, length, bredth):
        super().__init__(length, bredth=bredth)

    def area(self):
        return self.length * self.bredth

    def perimeter(self):
        return self.length * 2 * self.bredth


if __name__ == "__main__":
    c = circle(10)
    print(f"{c.area()      =}")  # 314.1592653589793
    print(f"{c.perimeter() =}")  # 62.83185307179586

    s = Square(10)
    print(f"{s.area()      =}")  # 100
    print(f"{s.perimeter() =}")  # 20

    r = Rectangle(10, 20)
    print(f"{r.area()      =}")  # 200
    print(f"{r.perimeter() =}")  # 400
