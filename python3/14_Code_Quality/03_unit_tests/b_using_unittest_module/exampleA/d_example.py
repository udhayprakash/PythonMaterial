#!/usr/bin/python
"""
Purpose: unit testing with unittest module
"""
import unittest


class TestSuite(unittest.TestCase):
    num1 = 50
    num2 = 40

    def test01_addition(self):
        """
        Logic for addition and its test
        """
        result = self.num1 + self.num2
        self.assertEqual(result, 90)

    @unittest.skipIf(num1 > num2, 'Skip over this routine')
    def test02_subtraction(self):
        result = self.num1 - self.num2
        self.assertTrue(result == -10)

    @unittest.skipUnless(num2 == 0, 'Skip over this routine')
    def test03_division(self):
        result = self.num1 / self.num2
        self.assertAlmostEqual(result, 1.249999999)
        self.assertTrue(result == 1)

    @unittest.expectedFailure
    def test04_mul(self):
        result = self.num1 * self.num2
        self.assertEqual(result == 0)


if __name__ == '__main__':
    unittest.main()
