#!/usr/bin/python
"""
Purpose: Unit testing using unittest module
"""
import unittest


def hello():
    print('Hello')


class SimpleHelloTest(unittest.TestCase):
    def test01_hello(self):
        assert hello() is None
        self.assertIsNone(hello())

    @unittest.skip("Incorrectly written. Need the team review")
    def test02_hello(self):
        assert hello() is not None
        self.assertIsNotNone(hello())


if __name__ == '__main__':
    unittest.main()
