#!/usr/bin/python 
"""
Purpose: Working with TestSuites
"""
import unittest


def function_test_1():
    name = 'mona'
    assert name.startswith('mo')


def compare_names(name1, name2):
    if name1 < name2:
        return 1
    elif name1 > name2:
        return -1
    else:
        return 0


class UnitTests02(unittest.TestCase):
    def testFoo(self):
        self.assertTrue(False)

    def checkBar01(self):
        self.assertFalse(False)


class UnitTests01(unittest.TestCase):
    # Note 1
    def setUp(self):
        print('setting up UnitTests01')

    def tearDown(self):
        print('tearing down UnitTests01')

    def testBar01(self):
        print('testing testBar01')
        self.assertFalse(False)

    def testBar02(self):
        print('testing testBar02')
        self.assertFalse(False)


def make_suite():
    suite = unittest.TestSuite()
    # Note 2
    suite.addTest(unittest.makeSuite(UnitTests01,
                                     sortUsing=compare_names))
    # Note 3
    suite.addTest(unittest.makeSuite(UnitTests02, prefix='check'))
    # Note 4
    suite.addTest(unittest.FunctionTestCase(function_test_1))
    return suite


def main():
    suite = make_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
