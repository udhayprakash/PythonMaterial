#!/usr/bin/python

__author__ = ""

import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_mul_method(self):
        self.assertEqual(4, self.calc.mul(2, 2))

    @classmethod
    def tearDownClass(cls):
        del cls.calc


if __name__ == "__main__":
    unittest.main()
