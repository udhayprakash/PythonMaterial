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


class TestMyClass:
    def test_addition(self):
        assert addition(10, 20) == 30

    def test1_addition(self):
        assert addition(10, 20) != 31

    def mytest1_addition(self):  # skipped
        assert addition(10, 20) == 31


"""
Grouping tests in classes can be beneficial for the following reasons:
    • Test organization
    • Sharing fixtures for tests only in that particular class
    • Applying marks at the class level and having them implicitly apply to all tests

"""
