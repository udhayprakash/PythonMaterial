#!/usr/bin/python3
"""
This script implements the unit testing for the tax_calculator.py script
"""
# Python Imports
import unittest

# Local imports
from tax_calculator import TaxCalculator


class TestTaxCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.tc = TaxCalculator()

    def test01_positive(self):
        self.assertEqual(self.tc.calculate_tax(1000), 150.0)
        self.assertEqual(self.tc.calculate_tax(10_000), 1500.0)
        self.assertEqual(self.tc.calculate_tax(100000), 17991.78)

    def test02_positive_edge_cases(self):
        self.assertEqual(self.tc.calculate_tax(214368), 49644.31)
        self.assertEqual(self.tc.calculate_tax(214369), 49644.64)

    def test03_positive_input_types(self):
        self.assertEqual(self.tc.calculate_tax(2000), 300.0)
        self.assertEqual(self.tc.calculate_tax(2000.0), 300.0)
        self.assertEqual(self.tc.calculate_tax("2000"), 300.0)
        self.assertEqual(self.tc.calculate_tax("2000.0"), 300.0)

    def test04_negative(self):
        invalid_message = "Invalid input"
        self.assertEqual(self.tc.calculate_tax("khgjhg"), invalid_message)
        self.assertEqual(self.tc.calculate_tax("545 876"), invalid_message)

    def test05_positive_valid_input(self):
        self.assertEqual(self.tc.calculate_tax("$2000"), 300.0)
        self.assertEqual(self.tc.calculate_tax("$ 2000"), 300.0)
        self.assertEqual(self.tc.calculate_tax("CAD2000"), 300.0)
        self.assertEqual(self.tc.calculate_tax("CAD 2000"), 300.0)
        self.assertEqual(self.tc.calculate_tax("cad2000"), 300.0)

    def test06_comma_in_input(self):
        self.assertEqual(self.tc.calculate_tax("2,000"), 300.0)
        self.assertEqual(self.tc.calculate_tax("545,876"), 159041.95)
        self.assertEqual(self.tc.calculate_tax("$2,000"), 300.0)

    def tearDown(self) -> None:
        del self.tc


if __name__ == "__main__":
    unittest.main()
