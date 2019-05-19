import unittest
import unittest_ex

class MyTest(unittest.TestCase):
    def testing_equaivalence(self):
        self.assertEqual(unittest_ex.fun(3), 4)

    def testing_not_equaivalence(self):
        self.assertNotEqual(unittest_ex.fun(3), 3)

if __name__ == '__main__':
    unittest.main()