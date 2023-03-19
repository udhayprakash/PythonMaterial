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
