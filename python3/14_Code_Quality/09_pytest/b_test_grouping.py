import pytest
from pytest import mark


@mark.positive
def test_add_pos_num():
    num1, num2 = 2, 4
    assert num1 + num2 == 6


@mark.negative
def test_add_neg_num():
    num1, num2 = -2, -4
    assert num1 + num2 == -6


"""
To run all,
    $ pytest

To run all in verbose mode,
    $ pytest -v

To run all test cases, under a group,
    $ pytest -m positive -v

To run and stop if atleast one test fails,
    $ pytest -maxfail 1 -v

To set the maximum test duration,
    $ pytest --duration=10


JUnit-Style Logs,
    $ py.test --junitxml=result.xml
"""
