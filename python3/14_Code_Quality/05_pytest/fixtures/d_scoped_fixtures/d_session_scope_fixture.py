"""
Purpose: session_scope_fixture
    - This fixture will run once per test session.
    - It can be used for setup that needs to be done once for all the tests in a test run.
    - For example, you might use this to set up a temporary directory for your tests to write files to.
"""
import tempfile

import pytest


@pytest.fixture(scope="session")
def temp_dir():
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir


class TestFileIO:
    def test_write_file(self, temp_dir):
        # Write a file to the temporary directory and verify it was written correctly
        pass

    def test_read_file(self, temp_dir):
        # Read a file from the temporary directory and verify its contents
        pass
