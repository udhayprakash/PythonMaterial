import unittest

class ArithTestSuper (unittest.TestCase):
    def setUp (self):
        print "Setting up ArithTest cases"

    def tearDown (self):
        print "Cleaning up ArithTest cases"

class ArithTest (ArithTestSuper):
    def runTest (self):
        """ Test addition and succeed. """
        print "Running ArithTest"
        self.failUnless (1+1==2, 'one plus one fails!')
        self.failIf (1+1 != 2, 'one plus one fails again!')
        self.failUnlessEqual (1+1, 2, 'more trouble with one plus one!')

class ArithTestFail (ArithTestSuper):
    def runTest (self):
        """ Test addition and fail. """
        print "Running ArithTestFail"
        self.failUnless (1+1==2, 'one plus one fails!')
        self.failIf (1+1 != 2, 'one plus one fails again!')
        self.failUnlessEqual (1+1, 2, 'more trouble with one plus one!')
        self.failIfEqual (1+1, 2, 'expected failure here')
        self.failIfEqual (1+1, 2, 'second failure')


class ArithTest2 (unittest.TestCase):
    def setUp (self):
        print "Setting up ArithTest2 cases"
    def tearDown (self):
        print "Cleaning up ArithTest2 cases"

    def runArithTest (self):
        """ Test addition and succeed, in one class. """
        print "Running ArithTest in ArithTest2"
        self.failUnless (1+1==2, 'one plus one fails!')
        self.failIf (1+1 != 2, 'one plus one fails again!')
        self.failUnlessEqual (1+1, 2, 'more trouble with one plus one!')

    def runArithTestFail (self):
        """ Test addition and fail, in one class. """
        print "Running ArithTestFail in ArithTest2"
        self.failUnless (1+1==2, 'one plus one fails!')
        self.failIf (1+1 != 2, 'one plus one fails again!')
        self.failUnlessEqual (1+1, 2, 'more trouble with one plus one!')
        self.failIfEqual (1+1, 2, 'expected failure here')
        self.failIfEqual (1+1, 2, 'second failure')


def suite():
    suite = unittest.TestSuite()

    # First style:
    suite.addTest (ArithTest())
    suite.addTest (ArithTestFail())

    # Second style:
    suite.addTest (ArithTest2("runArithTest"))
    suite.addTest (ArithTest2("runArithTestFail"))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)
