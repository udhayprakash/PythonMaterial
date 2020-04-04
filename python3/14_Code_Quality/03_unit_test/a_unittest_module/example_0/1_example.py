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
        self.assertEqual(addition(10, 20), 30)

    @unittest.skip("skipping for some reason")
    def test02_add_negative(self):
        self.assertNotEqual(addition(10, 20), 31)

    def test03_multiply_case(self):
        self.assertEqual(multiply(10, 20), 200)
        self.assertNotEqual(multiply(10, 20), 201)
        self.assertAlmostEqual(multiply(10, 20), 200.0)

    def test04_hello(self):
        self.skipTest("another method for skipping")
        self.assertIsNone(hello())
        self.assertIsNotNone(hello())


if __name__ == '__main__':
    unittest.main()
