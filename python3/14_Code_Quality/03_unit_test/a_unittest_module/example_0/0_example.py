#!/usr/bin/python
"""
Purpose: Unit testing
"""
import unittest


def addition(n1, n2):
    return n1 + n2


def multiply(v1, v2):
    return v1 * v2


def hello():
    print('Hello')


class SimpleTest(unittest.TestCase):
    def test01_add_positive(self):
        # assert addition(10, 20) == 30
        self.assertEqual(addition(10, 20), 30)

    def test02_add_negative(self):
        # self.assertEqual(addition(10, 20), 31)
        self.assertNotEqual(addition(10, 20), 31)

    def test03_multiply_case(self):
        # assert multiply(10, 20) == 200
        self.assertEqual(multiply(10, 20), 200)
        # assert multiply(10, 20) != 201
        self.assertNotEqual(multiply(10, 20), 201)
        self.assertAlmostEqual(multiply(10, 20), 200.0)

    def test04_hello(self):
        # assert hello() is None
        self.assertIsNone(hello())


if __name__ == '__main__':
    unittest.main()
