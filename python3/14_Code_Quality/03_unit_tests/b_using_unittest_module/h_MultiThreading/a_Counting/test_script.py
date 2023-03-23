import io
import sys
import unittest

from script import multithreaded_counting


class TestMultithreadedCounting(unittest.TestCase):
    def test_counts_up_to_10(self):
        with io.StringIO() as captured_output:
            # Redirect stdout to captured_output
            sys.stdout = captured_output

            multithreaded_counting(10)

            # Restore stdout
            sys.stdout = sys.__stdout__

            # Ensure that all numbers were printed
            self.assertEqual("0123456789", captured_output.getvalue().strip())

    def test_counts_up_to_100(self):
        with io.StringIO() as captured_output:
            # Redirect stdout to captured_output
            sys.stdout = captured_output

            multithreaded_counting(100, num_threads=4)

            # Restore stdout
            sys.stdout = sys.__stdout__

            # Ensure that all numbers were printed
            self.assertEqual(
                "".join(str(i) for i in range(100)), captured_output.getvalue().strip()
            )


if __name__ == "__main__":
    unittest.main()
