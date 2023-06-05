import unittest
from unittest.mock import Mock


def foo(some_object, number):
    if number > 2:
        some_object.method(number**2)  # foo.method(3)
    else:
        some_object.method(number - 1)


class MyClass:
    def __init__(self) -> None:
        self.val = 0

    def method(self, value):
        self.val = value


obj = MyClass()

foo(obj, 23)


class TestFoo(unittest.TestCase):
    def test_foo_for_2_calls_method_with_1(self):
        some_object = Mock(method=Mock())

        foo(some_object, 23)
        some_object.method.assert_called_once_with(1)
