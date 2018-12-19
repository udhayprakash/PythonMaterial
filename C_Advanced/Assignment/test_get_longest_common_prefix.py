import unittest
from get_longest_common_prefix import common_prefix, computation


class TestLongestCommonPrefix(unittest.TestCase):

    def test_positive_one(self):
        sample_data ={'amerigo', 'americ', 'ame', 'america', 'ame'}
        self.assertEqual(computation(sample_data), 'ame')

    def test_positive_two(self):
        sample_data = {'apple', 'ape', 'april'}
        self.assertEqual(computation(sample_data), 'ap')

    def test_negative_one(self):
        sample_data ={'amerigo', 'americ', 'ame', 'america', 'ame'}
        self.assertNotEqual(computation(sample_data), 'amer')

    def test_negative_two(self):
        sample_data = {'apple', 'ape', 'april'}
        self.assertNotEqual(computation(sample_data), 'app')

