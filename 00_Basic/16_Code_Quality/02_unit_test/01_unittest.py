import unittest


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def testing_equaivalence(self):
        self.assertEqual(fun(3), 4)
