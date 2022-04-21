#!/usr/bin/python
"""
Purpose:
"""
from unittest import TestCase, main
from unittest.mock import Mock, patch, PropertyMock


class Foo:
    x = 10


class Bar:
    x = 20


class MyTest(TestCase):
    """
    To mock one callable object with another
    """

    @patch("__main__.Foo", new_callable=Bar)
    def test_name_1(self, mock_foo):
        pass


# -------------------------------------
@property
def foo(self):
    return "Hello"


class TestFoo(TestCase):
    @patch("__main__.foo", new_callable=PropertyMock)
    def test_foo(self, mock_foo):
        pass


if __name__ == "__main__":
    main()
