import unittest

from printing import multithreaded_printing


class TestMultithreadedPrinting(unittest.TestCase):
    def test_prints_hello_world_4_times_with_2_threads(self):
        multithreaded_printing("Hello, world!", 4)
        # Ensure that the message was printed the correct number of times
        self.assertEqual(
            "Hello, world!\nHello, world!\nHello, world!\nHello, world!",
            captured_output.getvalue().strip(),
        )

    def test_prints_hi_10_times_with_5_threads(self):
        multithreaded_printing("Hi!", 10, num_threads=5)
        # Ensure that the message was printed the correct number of times
        self.assertEqual(
            "Hi!\nHi!\nHi!\nHi!\nHi!\nHi!\nHi!\nHi!\nHi!\nHi!",
            captured_output.getvalue().strip(),
        )


if __name__ == "__main__":
    unittest.main()
