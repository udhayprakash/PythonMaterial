"""
Purpose: Testing multiplication functionality in calculator
"""
import sys
import unittest

sys.path.insert(0, "..")

from calculator import multiplication


class TestSuitemultiplication(unittest.TestCase):
    def test01(self):
        self.assertEqual(multiplication(10, 20), 200)

    def test02(self):
        self.assertEqual(multiplication(10, 20.0), 200.0)
        self.assertEqual(multiplication(10.0, 20), 200.0)
        self.assertEqual(multiplication(10.0, 20.0), 200.0)

    def test03(self):
        self.assertEqual(multiplication(10.0, "20"), 200.0)
        self.assertEqual(multiplication("10", "20"), 200.0)

        self.assertEqual(multiplication("10.0", 20), 200.0)
        self.assertEqual(multiplication("10.0", "20.0"), 200.0)

    @unittest.expectedFailure
    def test04(self):
        self.assertEqual(multiplication("10.0", True), 200.0)
