# python -m mypy script.py


def addition(n1: int, n2: int) -> int:
    return n1 + n2


print(addition(10, 20))
# print(addition(10.3, 20.4))


def additionFloat(n1: float, n2: float) -> float:
    return n1 + n2


print(additionFloat(10, 20))
print(additionFloat(10.3, 20.4))


def concat(a: str, b: str) -> str:
    return a + b


concat("foo", "bar")  # Ok, output has type 'unicode'
# concat(b"foo", b"bar")  # Ok, output has type 'bytes'
# concat(u"foo", b"bar")  # Error, cannot mix unicode and bytes


from typing import AnyStr


def concatAny(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b


concatAny("foo", "bar")  # Ok, output has type 'unicode'
concatAny(b"foo", b"bar")  # Ok, output has type 'bytes'
# concatAny(u"foo", b"bar")  # Error, cannot mix unicode and bytes


from typing import Any


def hello_world(name: Any) -> str:
    return f"{name = }"


hello_world("Pyton")
hello_world(21)
hello_world(21.23)
hello_world(True)


# Any two specific types
from typing import Union


def helloworldTHREETYPES(name: Union[int, str, float]) -> str:
    return f"{name = }"


helloworldTHREETYPES("Pyton")
helloworldTHREETYPES(21)
helloworldTHREETYPES(21.23)
helloworldTHREETYPES(True)  # bool is also of type int


# in python 3.9, new opeertor was created for Union


def helloworldTHREETYPES2(name: int | str | float) -> str:
    return f"{name = }"


helloworldTHREETYPES2("Pyton")
helloworldTHREETYPES2(21)
helloworldTHREETYPES2(21.23)
helloworldTHREETYPES2(True)  # bool is also of type int

from typing import Optional


def hello_word(name: Optional[str] = "world") -> str:
    return f"Hello {name}"


print(hello_word("Python"))
print(hello_word())

from typing import List

# def average(nums: List[int]) -> float:
#     return sum(nums)/len(nums)


# print(average([1, 2, 3, 4, 5, ]))
# print(average([213]))
# print(average([]))


def average(nums: List[int]) -> float | ZeroDivisionError:
    return sum(nums) / len(nums)


print(
    average(
        [
            1,
            2,
            3,
            4,
            5,
        ]
    )
)
print(average([213]))
try:
    print(average([]))
except ZeroDivisionError:
    print("DOnt pass empty list")


# -- *args & kwargs
from typing import Tuple


def print_function1(*args: Tuple[int]) -> None:
    print("args", args)


print_function1((0,))
print_function1((1,))


def print_function2(*args: Tuple[int, int]) -> None:
    print("args", args)


print_function2((0, 1))
print_function2((1, 2))


def print_function3(*args: Tuple[int, ...]) -> None:
    print("args", args)


print_function3((0,))
print_function3((0, 1))
print_function3((1, 2, 3, 4, 5))


from typing import Sequence


# Sequence - Either list or tuple
def print_functionSequence(args: Sequence[int]) -> None:
    print("args", args)


print_functionSequence([1, 2, 3])  # list of int
print_functionSequence((1, 2, 3))  # tuplr of int
print_functionSequence((1, 2, 3, 3, 3, 123, 23))  # lt uple
# print_functionSequence({21, 2, 3, })
# print_functionSequence(1, 2, 3, 3, 3, 123, 23, 'asd')


def print_functionAnyNo(*args: Tuple[int, ...]) -> None:
    print("args", args)


print_functionAnyNo()  # tuplr of int
print_functionAnyNo((1,))  # tuplr of int
print_functionAnyNo((1, 2, 3))  # tuplr of int
# print_functionAnyNo(1, 2, 3)


from typing import Dict, Sequence


def print_functionAny(
    *args: Any, **kwargs: Any  # Tuple[int, ...],  # Dict[str, str]   # TODO
) -> None:
    print("args", args)
    print("kwargs", kwargs)


print_functionAny()
print_functionAny(1)
print_functionAny(1, 2, 3)
print_functionAny(1, 2, 3, name="udhay")


from typing import NoReturn


def stop() -> NoReturn:
    raise RuntimeError("no way")


from typing import ClassVar, Optional, Self


class Car:
    model_name: ClassVar[str] = "BMW"

    def __init__(self: Self, car_number: Optional[int] = 21312312) -> None:
        # self.car_number: int = car_number
        self.car_number: Optional[int] = car_number


from typing import Final

MAX_SIZE: Final = 9000
# MAX_SIZE += 1  # Error reported by type checker

# ------------- GENERATORS

from typing import Generator

# Generator[YieldType, SendType, ReturnType]


def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return "Done"


def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1


from typing import Iterator


def infinite_stream2(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1
