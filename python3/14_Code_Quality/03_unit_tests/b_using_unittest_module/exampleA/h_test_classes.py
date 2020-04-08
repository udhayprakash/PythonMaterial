#!/usr/bin/python
"""
Purpose: unit testing

setupClass & tearDownClass methods are executed ONCE, per test suite
setUp & tearDown methods are executed for each test case
"""

import unittest


class TestSuiteDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass method executed ...')

    def setUp(self):
        print('\nsetUp method execution ...')

    def test_method1(self):
        print('test method 1')

    def test_method2(self):
        print('test method 2')

    def tearDown(self) -> None:
        print('tearDown method execution ...')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass method executed ...')


if __name__ == '__main__':
    unittest.main()
