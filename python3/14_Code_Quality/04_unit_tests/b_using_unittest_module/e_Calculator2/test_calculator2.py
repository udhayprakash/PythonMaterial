import unittest

import calculator


class TestAddition(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.calc = calculator.ArithmeticOperations()

    def test01_add_positive(self):
        self.assertEqual(self.calc.addition(10, 20), 30)
        self.assertEqual(self.calc.addition(20, 10), 30)

    def test02_add_negative(self):
        self.assertEqual(self.calc.addition(20, -10), 10)
        self.assertEqual(self.calc.addition(-10, 20), 10)
        self.assertEqual(self.calc.addition(-20, -10), -30)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.calc
