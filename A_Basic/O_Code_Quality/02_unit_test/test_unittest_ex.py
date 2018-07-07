import unittest
import unittest_ex

class MyTest(unittest.TestCase):
    def testing_equaivalence(self):
        self.assertEqual(
            unittest_ex.fun(3), 4)

if __name__ == '__main__':
    unittest.main()