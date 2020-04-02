#!/usr/bin/python
"""
Purpose: unit testing
"""

import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('\nsetUp method execution ...')

    def test_method1(self):
        print('test method 1')

    def test_method2(self):
        print('test method 2')

    def tearDown(self) -> None:
        print('tearDown method execution ...')


if __name__ == '__main__':
    unittest.main()
