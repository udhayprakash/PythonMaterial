#!/usr/bin/python
"""
Purpose: unit tests for person.py file
"""
import unittest
from person import Person


class TestingPerson(unittest.TestCase):
    def setUp(self):
        self.p = Person()

    def testing_functionality(self):
        test_name = 'Prakash'
        user_id = self.p.set_name(test_name)
        self.assertEqual(self.p.get_name(user_id), test_name)

    def testing_list_of_names(self):
        test_names = ['Udhay', 'Syed', 'Baseer', 'Hero', 'Prakash', 'Jameel']
        for test_name in test_names:
            user_id = self.p.set_name(test_name)
            self.assertEqual(self.p.get_name(user_id), test_name)

    def testing_list_wise(self):
        test_names = ['Udhay', 'Syed', 'Baseer', 'Hero', 'Prakash', 'Jameel']
        retrieved_names = []
        for test_name in test_names:
            user_id = self.p.set_name(test_name)
            retrieved_names.append(self.p.get_name(user_id))
        self.assertListEqual(retrieved_names, test_names)

    def test_user_id_greater_than_len(self):
        self.assertEqual(self.p.get_name(-1), 'There is no such user')


if __name__ == '__main__':
    unittest.main(verbosity=4)
