"""
Purpose: Duck Typing

    Duck Typing refers to the principle of not constraining or binding
    the code to specific data types.



"""


class Duck:
    def swim(self):
        print("Duck swimming")

    def fly(self):
        print("Duck flying")


class Whale:
    def swim(self):
        print("Whale swimming")


for animal in [Duck(), Whale()]:
    animal.swim()
    animal.fly()
