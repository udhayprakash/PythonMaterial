import multiprocessing
import unittest


def sum_numbers(a, b):
    return a + b


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1, 2), 3)
        self.assertEqual(sum_numbers(2, 3), 5)
        self.assertEqual(sum_numbers(3, 4), 7)

    def test_sum_numbers_multiprocessing(self):
        with multiprocessing.Pool(processes=2) as pool:
            results = pool.starmap(sum_numbers, [(1, 2), (2, 3), (3, 4)])
            self.assertEqual(results, [3, 5, 7])
            self.assertListEqual(results, [3, 5, 7])
