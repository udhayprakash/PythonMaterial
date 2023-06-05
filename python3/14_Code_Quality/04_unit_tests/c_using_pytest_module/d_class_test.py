#!/usr/bin/python3
"""
Purpose: Grouping the test functions
    - Test cases can be binded in a single class
    - Naming convention
        - class name  should start with 'Test'
        - methods names should start with 'test_'
        - Else they will be skipped
"""


def addition(n1, n2):
    return n1 + n2


def test_addition():
    assert addition(1, 2) == 3


def test_addition2():
    assert addition(10, 20) == 30


def mytest_addition():  # skipped
    assert addition(-1, -2) == -3


class TestAddition:
    def test_addition(self):
        assert addition(1, 2) == 3

    def test_addition2(self):
        assert addition(10, 20) == 30

    def mytest_addition(self):  # skipped
        assert addition(-1, -2) == -3


# Assigned - in constructor create addition - wrte test cases - one for value, one type


"""
Grouping tests in classes can be beneficial for the following reasons:
    • Test organization
    • Sharing fixtures for tests only in that particular class
    • Applying marks at the class level and having them implicitly apply to all tests

"""
