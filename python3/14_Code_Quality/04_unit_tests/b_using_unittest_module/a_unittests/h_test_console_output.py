import sys
import unittest
from io import StringIO


def hello():
    # print("Hello!")
    print("Hello!", file=sys.stdout)


class TestHello(unittest.TestCase):
    def test01_hello_result_equal_check(self):
        assert hello() == None
        self.assertEqual(hello(), None)

    def test02_hello_result_identity_check(self):
        assert hello() is None
        self.assertIsNone(hello())

    @unittest.skip("Incorrectly written. Need the team review")
    def test03_negative(self):
        # assert hello() is not None
        self.assertIsNotNone(not hello())

    def test04_print_output_check(self):
        # Redirect stdout and stderr to StringIO buffers
        with StringIO() as stdout_buffer, StringIO() as stderr_buffer:
            sys.stdout = stdout_buffer
            sys.stderr = stderr_buffer

            # Call the function that prints output
            hello()

            # Get the captured output from the buffers
            stdout_output = stdout_buffer.getvalue()
            stderr_output = stderr_buffer.getvalue()

            # Reset stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            # Assert that the output contains the expected substring
            self.assertIn("Hello!", stdout_output)
