import unittest
from unittest.mock import patch

import calculator


class TestSubtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.calc = calculator.ArithmeticOperations()

    def test01_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 20), -10)

    @patch("calculator.ArithmeticOperations.subtraction")
    def test02_subtraction_patch(self, mock_subtraction):
        print("test02_subtraction_patch")
        mock_subtraction.return_value = -10
        self.assertEqual(self.calc.subtraction(10, 20), -10)

    @patch("calculator.ArithmeticOperations.subtraction", return_value=-10)
    def test03_subtraction_patch(self, mock_subtraction):
        print("test03_subtraction_patch")
        self.assertEqual(self.calc.subtraction(10, 20), -10)


# function
# variable
