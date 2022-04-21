import pytest
from pytest import mark


def add(a, b):
    return a+b


@mark.parametrize('num1, num2, expected',
                  [(2, 5, 7), (3, 7, 10)])
def test_addition(num1, num2, expected):
    assert add(num1, num2) == expected
