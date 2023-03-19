#!/usr/bin/python
"""
Purpose: Unit testing using unittest module
"""
import unittest


def hello():
    print("Hello!")


class TestHello(unittest.TestCase):
    def test01_hello_result_equal_check(self):
        assert hello() == None
        self.assertEqual(hello(), None)

    def test02_hello_result_identity_check(self):
        assert hello() is None
        self.assertIsNone(hello())

    @unittest.skip("Incorrectly written. Need the team review")
    def test03_negative(self):
        # assert hello() is not None
        self.assertIsNotNone(hello())


if __name__ == "__main__":
    unittest.main()
