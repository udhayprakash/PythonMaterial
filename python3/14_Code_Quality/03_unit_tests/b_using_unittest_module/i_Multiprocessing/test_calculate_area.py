import unittest

from calculate_area import calculate_area_parallel


class TestCalculateAreaParallel(unittest.TestCase):
    def test_calculate_area_parallel(self):
        result = calculate_area_parallel([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [4, 10, 18])

    def test_calculate_area_parallel2(self):
        lengths = [2, 3, 4]
        widths = [3, 4, 5]
        expected_output = [6, 12, 20]

        result = calculate_area_parallel(lengths, widths)
        self.assertEqual(result, expected_output)

    def test_calculate_area_parallel_empty_input(self):
        lengths = []
        widths = []
        expected_output = []
        result = calculate_area_parallel(lengths, widths)
        self.assertEqual(result, expected_output)

    def test_calculate_area_parallel_invalid_input(self):
        lengths = [2, 3, 4]
        widths = [3, 4]
        with self.assertRaises(ValueError):
            result = calculate_area_parallel(lengths, widths)
            print(result)
