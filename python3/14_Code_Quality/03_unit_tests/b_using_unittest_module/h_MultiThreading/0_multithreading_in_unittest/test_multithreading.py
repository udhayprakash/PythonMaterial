import unittest
from concurrent.futures import ThreadPoolExecutor


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertTrue("HELLO".isupper())
        self.assertFalse("Hello".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_join(self):
        self.assertEqual(" ".join(["hello", "world"]), "hello world")
        self.assertEqual("".join(["hello", "world"]), "helloworld")

    def test_replace(self):
        self.assertEqual("hello, world".replace("world", "python"), "hello, python")
        self.assertEqual("hello, world".replace("l", "x"), "hexxo, worxd")

    def test_strip(self):
        self.assertEqual("   hello   ".strip(), "hello")
        self.assertEqual("   hello   ".lstrip(), "hello   ")
        self.assertEqual("   hello   ".rstrip(), "   hello")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit each test method to the executor
        futures = [executor.submit(test_method) for test_method in suite]

        # Wait for all tests to complete and retrieve their results
        results = [future.result() for future in futures]

    # Count the number of failed tests
    failed_count = sum(1 for result in results if result.errors or result.failures)
    print(f"Finished {len(results)} tests with {failed_count} failures.")
