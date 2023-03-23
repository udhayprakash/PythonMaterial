"""
Purpose:


self.assertWarns(expected_warning, callable, *args, **kwargs) - Checks that the callable callable raises a warning of type expected_warning when called with the arguments args and keyword arguments kwargs.
self.assertLogs(logger=None, level=None) - Checks that messages have been logged to the specified logger at the specified level. This method can be used to test logging output.
self.assertWarnsRegex(expected_warning, regex, callable, *args, **kwargs) - Checks that the callable callable raises a warning of type expected_warning with a message that matches the regular expression regex when called with the arguments args and keyword arguments kwargs.
self.assertRaises(exception, callable, *args, **kwargs) - Checks that the callable callable raises an exception of type exception when called with the arguments args and keyword arguments kwargs.
self.assertRaisesRegex(exception, regex, callable, *args, **kwargs) - Checks that the callable callable raises an exception of type exception with a message that matches the regular expression regex when called with the arguments args and keyword arguments kwargs.
self.assertLogs(logger=None, level=None) - Checks that messages have been logged to the specified logger at the specified level. This method can be used to test logging output.
self.assertDictContainsSubset(subset, dictionary) - Checks that the dictionary subset is a subset of the dictionary dictionary. This method checks that all the key-value pairs in subset are present in dictionary, but dictionary may contain additional key-value pairs not in subset.


"""

import logging
import unittest


def my_function(x):
    if x < 0:
        logging.warning("Negative value provided")
    return x**2


class TestMyFunction(unittest.TestCase):
    def test_positive_value(self):
        result = my_function(2)
        self.assertEqual(result, 4)

    def test_negative_value(self):
        with self.assertWarns(UserWarning):
            result = my_function(-2)
        self.assertEqual(result, 4)

    def test_logging(self):
        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.WARNING)
        with self.assertLogs(logger=logger, level="WARNING") as cm:
            my_function(-2)
        self.assertIn("Negative value provided", cm.output[0])

    def test_regex(self):
        with self.assertWarnsRegex(UserWarning, "Negative value.*"):
            result = my_function(-2)
        self.assertEqual(result, 4)

    def test_dict_subset(self):
        d1 = {"a": 1, "b": 2, "c": 3}
        d2 = {"a": 1, "c": 3}
        self.assertDictContainsSubset(d2, d1)


if __name__ == "__main__":
    unittest.main()
