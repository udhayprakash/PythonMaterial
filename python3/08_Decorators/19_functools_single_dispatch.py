from functools import singledispatch
from datetime import date, datetime, time

# To overload the format() function.
# Though it is generally not possible, here using singledispatch,
# we can achive it


@singledispatch
def format(arg):
    return arg


@format.register
def _(arg: date):
    return f'{arg.day}-{arg.month}-{arg.year}'


@format.register
def _(arg: datetime):
    return f'{arg.day}-{arg.month}-{arg.year} {arg.hour}:{arg.minute}:{arg.second}'


@format.register(time)
def _(arg):
    return f'{arg.hour}:{arg.minute}:{arg.second}'


if __name__ == '__main__':
    print(format('today'))  # today
    print(format(date(2021, 5, 26)))  # 26-5-2021
    print(format(datetime(2021, 5, 26, 17, 25, 10)))  # 26-5-2021 17:25:10
    print(format(time(19, 22, 15)))  # 19:22:15
