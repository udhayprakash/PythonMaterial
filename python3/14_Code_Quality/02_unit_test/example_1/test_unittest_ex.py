import unittest
import unittest_ex


class MyTest(unittest.TestCase):
    def testing_equaivalence(self):
        self.assertEqual(unittest_ex.fun(3), 4)

    def testing_not_equaivalence(self):
        self.assertNotEqual(unittest_ex.fun(3), 3)

    def testing_equaivalence_2(self):
        self.assertEqual(unittest_ex.fun(-0.2), 0.8)


if __name__ == '__main__':
    unittest.main()
