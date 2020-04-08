#!/usr/bin/python
"""
Purpose:
"""
import unittest

from script import add_one

print(f'add_one(12):{add_one(12)}')


class MyTestSuite(unittest.TestCase):
    def testing01_equivalence(self):
        self.assertEqual(add_one(3), 4)

    def testing02_equivalence(self):
        self.assertEqual(add_one(-0.2), 0.8)

    def testing03_equivalence(self):
        self.assertNotEqual(add_one(-0.2), -1.2)


if __name__ == '__main__':
    unittest.main()
