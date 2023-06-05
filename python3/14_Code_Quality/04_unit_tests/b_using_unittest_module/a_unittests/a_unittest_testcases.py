import unittest

# print(dir(unittest))
# help(unittest)

print(f"{2 + 3 == 5 = }")  # True
assert 2 + 3 == 5


class TestAddition(unittest.TestCase):
    def test_addition_positive(self):
        self.assertEqual(2 + 3, 5)


choice1 = True
choice2 = False
assert choice1 != choice2


class TestCheck(unittest.TestCase):
    def test_booleans(self):
        choice1 = True
        choice2 = False
        self.assertNotEqual(choice1, choice2)
        self.assertNotEqual(choice1, False)
        self.assertNotEqual(choice2, True)
        self.assertEqual(choice2, False)

    def test_two_strings(self):
        self.assertEqual("", "")
        self.assertNotEqual("", " ")
        self.assertNotEqual("-", "~")
        self.assertNotEqual("Udhay", "udhay")


if __name__ == "__main__":
    unittest.main(verbosity=4)

"""
self.assertEqual(a, b) - Checks that a is equal to b
self.assertNotEqual(a, b) - Checks that a is not equal to b
self.assertTrue(x) - Checks that x is true
self.assertFalse(x) - Checks that x is false
self.assertIs(a, b) - Checks that a is the same object as b
self.assertIsNot(a, b) - Checks that a is not the same object as b
self.assertIn(a, b) - Checks that a is a member of b
self.assertNotIn(a, b) - Checks that a is not a member of b
self.assertGreater(a, b) - Checks that a is greater than b
self.assertGreaterEqual(a, b) - Checks that a is greater than or equal to b
self.assertLess(a, b) - Checks that a is less than b
self.assertLessEqual(a, b) - Checks that a is less than or equal to b
self.assertRegex(s, r) - Checks that s matches the regular expression r
self.assertNotRegex(s, r) - Checks that s does not match the regular expression r
self.assertCountEqual(a, b) - Checks that a and b have the same elements, ignoring order

self.assertAlmostEqual(a, b) - Checks that a is approximately equal to b. This method is useful for comparing floating-point numbers, where small differences may be expected due to rounding errors.
self.assertNotAlmostEqual(a, b) - Checks that a is not approximately equal to b.
self.assertDictEqual(a, b) - Checks that the dictionaries a and b have the same keys and values.
self.assertListEqual(a, b) - Checks that the lists a and b have the same elements in the same order.
self.assertTupleEqual(a, b) - Checks that the tuples a and b have the same elements in the same order.
self.assertSetEqual(a, b) - Checks that the sets a and b have the same elements, regardless of order.
self.assertSequenceEqual(a, b) - Checks that the sequences a and b have the same elements in the same order. This method works with any iterable type, including lists, tuples, and sets.
self.assertMultiLineEqual(a, b) - Checks that the strings a and b are equal, ignoring differences in line endings (i.e., \n versus \r\n).

self.assertWarns(expected_warning, callable, *args, **kwargs) - Checks that the callable callable raises a warning of type expected_warning when called with the arguments args and keyword arguments kwargs.
self.assertLogs(logger=None, level=None) - Checks that messages have been logged to the specified logger at the specified level. This method can be used to test logging output.
self.assertWarnsRegex(expected_warning, regex, callable, *args, **kwargs) - Checks that the callable callable raises a warning of type expected_warning with a message that matches the regular expression regex when called with the arguments args and keyword arguments kwargs.
self.assertRaises(exception, callable, *args, **kwargs) - Checks that the callable callable raises an exception of type exception when called with the arguments args and keyword arguments kwargs.
self.assertRaisesRegex(exception, regex, callable, *args, **kwargs) - Checks that the callable callable raises an exception of type exception with a message that matches the regular expression regex when called with the arguments args and keyword arguments kwargs.
self.assertLogs(logger=None, level=None) - Checks that messages have been logged to the specified logger at the specified level. This method can be used to test logging output.
self.assertDictContainsSubset(subset, dictionary) - Checks that the dictionary subset is a subset of the dictionary dictionary. This method checks that all the key-value pairs in subset are present in dictionary, but dictionary may contain additional key-value pairs not in subset.


"""
