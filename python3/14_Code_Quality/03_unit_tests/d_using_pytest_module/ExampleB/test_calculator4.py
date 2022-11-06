import math
import unittest

from calculator import ArithmeticOperations


class TestMultiplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mul = ArithmeticOperations().multiplication

    def test01_multiplication(self):
        assert self.mul(10, 20) == 200
        self.assertEqual(self.mul(10, 20), 200)

    def test02_multiplication(self):
        self.assertAlmostEqual(
            self.mul(10.123123123123123, 213213213123.213123), 2158383607922.9775
        )

    def test03_multiplication(self):
        self.assertEqual(self.mul(math.inf, 234234), math.inf)

    @unittest.expectedFailure
    def test04_multiplication(self):
        self.assertEqual(self.mul("10.0", True), 200.0)
