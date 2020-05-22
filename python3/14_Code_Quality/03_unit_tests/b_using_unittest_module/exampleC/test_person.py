#!/usr/bin/python 
"""
Purpose: unit tests for person.py file 
"""
import unittest
from person import Person


class TestingPerson(unittest.TestCase):
    def testing_functionality(self):
        test_name = 'Prakash'
        p = Person()
        user_id = p.set_name(test_name)
        # print('p.get_name(user_id)', p.get_name(user_id))
        self.assertEqual(p.get_name(user_id), test_name)

    def testing_list_of_names(self):
        test_names = ['Udhay', 'Syed', 'Baseer', 'Hero', 'Prakash', 'Jameel']
        p = Person()
        for test_name in test_names:
            user_id = p.set_name(test_name)
            # print(f'{user_id =} {p.get_name(user_id) =}')
            self.assertEqual(p.get_name(user_id), test_name)

    def testing_list_wise(self):
        test_names = ['Udhay', 'Syed', 'Baseer', 'Hero', 'Prakash', 'Jameel']
        p = Person()
        retrieved_names = []
        for test_name in test_names:
            user_id = p.set_name(test_name)
            # print(f'{user_id =} {p.get_name(user_id) =}')
            retrieved_names.append(p.get_name(user_id))
        # print(f'{test_names      =}')
        # print(f'{retrieved_names =}')
        self.assertListEqual(retrieved_names, test_names)

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main(verbosity=4)