import unittest

from stock_problem import solution1, solution2


class TestLongestCommonPrefix(unittest.TestCase):

    def test_positive_one(self):
        sample_data = [7, 6, 4, 3, 1]
        self.assertEqual(solution1(sample_data), 0)

    def test_positive_two(self):
        sample_data = [7, 6, 4, 3, 1]
        self.assertEqual(solution2(sample_data), 0)

    def test_positive_three(self):
        sample_data = [2, 1, 2, 0, 1]
        self.assertEqual(solution1(sample_data), 2)

    def test_positive_four(self):
        sample_data = [2, 1, 2, 0, 1]
        self.assertEqual(solution2(sample_data), 2)