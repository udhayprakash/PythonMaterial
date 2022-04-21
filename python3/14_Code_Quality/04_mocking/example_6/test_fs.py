from unittest import TestCase, main, mock
import fs


class TestExamples(TestCase):
    @mock.patch("example_6.fs.check_ouput", return_value="foo\nbar\n")
    def test_print_contents_of_cwd_success(self, mock_check_output):
        actual_result = fs.print_contents_of_cwd()

        expected_directory = b"tests"
        self.assertIn(expected_directory, actual_result)


@mock.patch("example_6.fs.check_ouput", return_value="foo\nbar\n")
class TestExamples2(TestCase):
    def test_print_contents_of_cwd_success(self, mock_check_output):
        actual_result = fs.print_contents_of_cwd()

        expected_directory = b"tests"
        self.assertIn(expected_directory, actual_result)
