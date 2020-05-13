#!/usr/bin/python
import unittest
from mymod import is_anagram


class TestAnagram(unittest.TestCase):
    def test_anagram_positive(self):
        self.assertTrue(is_anagram("abc", "acb"))
        self.assertTrue(is_anagram("bat", "tab"))
        self.assertTrue(is_anagram("silent", "listen"))

    def test_anagram_negative(self):
        self.assertFalse(is_anagram("one", "two"))


if __name__ == '__main__':
    unittest.main()
