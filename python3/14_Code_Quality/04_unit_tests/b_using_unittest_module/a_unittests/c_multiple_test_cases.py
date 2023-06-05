import unittest


class TestMyAsserts(unittest.TestCase):
    def test_assertAlmostEqual(self):
        a = 0.1 + 0.1 + 0.1
        b = 0.3
        self.assertAlmostEqual(a, b)

    def test_assertNotAlmostEqual(self):
        a = 0.1 + 0.1 + 0.1
        b = 0.2
        self.assertNotAlmostEqual(a, b)

    def test_assertDictEqual(self):
        a = {"a": 1, "b": 2, "c": 3}
        b = {"b": 2, "c": 3, "a": 1}
        self.assertDictEqual(a, b)

    def test_assertListEqual(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertListEqual(a, b)

    def test_assertTupleEqual(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b)

    def test_assertSetEqual(self):
        a = {1, 2, 3}
        b = {3, 2, 1}
        self.assertSetEqual(a, b)

    def test_assertSequenceEqual(self):
        a = [1, 2, 3]
        b = (1, 2, 3)
        self.assertSequenceEqual(a, b)

    def test_assertMultiLineEqual(self):
        a = "Line 1\nLine 2\nLine 3\n"
        b = "Line 1\r\nLine 2\r\nLine 3\r\n"
        self.assertMultiLineEqual(a, b.replace("\r\n", "\n"))


if __name__ == "__main__":
    unittest.main()
