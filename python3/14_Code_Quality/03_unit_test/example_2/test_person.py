import unittest
from person import Person


class TestingPerson(unittest.TestCase):
    def testing_functionality(self):
        test_name = 'bhavya'
        p = Person()
        # print 'p.name', p.name
        # print 'callable(p.set_name)', callable(p.set_name)
        user_id = p.set_name(test_name)
        print('p.get_name(user_id)', p.get_name(user_id))
        self.assertEqual(test_name, p.get_name(user_id))


# class Testing(unittest.TestCase):
#     def test_string(self):
#         a = 'some'
#         b = 'some'
#         self.assertEqual(a, b)

#     def test_boolean(self):
#         a = True
#         b = True
#         self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
