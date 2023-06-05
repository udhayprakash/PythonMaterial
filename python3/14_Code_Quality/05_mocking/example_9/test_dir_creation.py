import unittest
from unittest.mock import patch

from dir_creation import make_directory


class MyTest(unittest.TestCase):
    @patch("os.path.exists")
    @patch("os.makedirs")
    def test_create_dir(self, mock_make_dirs, mock_exists):
        mock_exists.return_value = True

        make_directory("thing_to_create")

        mock_exists.assert_called_with("thing_to_create")
        # mock_make_dirs.assert_called_with('thing_to_create')
