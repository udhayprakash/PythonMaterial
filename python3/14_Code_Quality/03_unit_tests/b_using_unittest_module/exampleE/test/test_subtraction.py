#!/usr/bin/python
"""
Purpose: Testing subtraction functionality in calculator
"""
from calculator import subtraction
import sys
import unittest


sys.path.insert(0, "..")


class TestSuitesubtraction(unittest.TestCase):
    def test01(self):
        self.assertEqual(subtraction(10, 20), -10)

    def test02(self):
        self.assertEqual(subtraction(10, 20.0), -10.0)
        self.assertEqual(subtraction(10.0, 20), -10.0)
        self.assertEqual(subtraction(10.0, 20.0), -10.0)

    def test03(self):
        self.assertEqual(subtraction(10.0, "20"), -10.0)
        self.assertEqual(subtraction("10", "20"), -10.0)

        self.assertEqual(subtraction("10.0", 20), -10.0)
        self.assertEqual(subtraction("10.0", "20.0"), -10.0)

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(subtraction("10.0", True), -10.0)
