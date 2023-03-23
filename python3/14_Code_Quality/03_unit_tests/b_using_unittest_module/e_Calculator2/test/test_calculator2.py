import unittest

from ExampleB.calculator import ArithmeticOperations


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("TestCalculator - SetUpClass")
        cls.calc = ArithmeticOperations()

    def test01_addition(self):
        self.assertEqual(self.calc.addition(10, 20), 30)
