import unittest


class suiteTest(unittest.TestCase):
    a = 50
    b = 40

    def testadd(self):
        """Add"""
        result = self.a + self.b
        self.assertEqual(result, 100)

    @unittest.skipIf(a > b, "Skip over this routine")
    def testsub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)

    @unittest.skipUnless(b == 0, "Skip over this routine")
    def testdiv(self):
        """div"""
        result = self.a / self.b
        self.assertTrue(result == 1)

    @unittest.expectedFailure
    def testmul(self):
        """mul"""
        result = self.a * self.b
        self.assertEqual(result == 0)


if __name__ == '__main__':
    unittest.main()
