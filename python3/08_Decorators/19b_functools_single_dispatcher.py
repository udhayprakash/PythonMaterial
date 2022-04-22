from datetime import date, time
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    def format(self, arg):
        raise NotImplementedError(f"Cannot format value of type {type(arg)}")

    @format.register
    def _(self, arg: date):
        return f"{arg.day}-{arg.month}-{arg.year}"

    @format.register
    def _(self, arg: time):
        return f"{arg.hour}:{arg.minute}:{arg.second}"


f = Formatter()
print(f.format(date(2021, 5, 26)))  # 26-5-2021
print(f.format(time(19, 22, 15)))  # 19:22:15
