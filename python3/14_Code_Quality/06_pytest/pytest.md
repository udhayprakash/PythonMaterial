## Anatomy of a test

- Tests are broken into FOUR steps:
  1.  Arrange
      - mean preparing objects,
      - starting/killing services,
      - entering records into a database, or
      - defining a URL to query,
      - generating some credentials for a user that doesn’t exist yet, or
      - just waiting for some process to finish.
  2.  Act
      - singular, state-changing action that kicks off the behavior we want to test
  3.  Assert
      - It’s where we gather evidence to say the behavior does or does not aligns with what we expect.
  4.  Cleanup
      - where the test picks up after itself, so other tests aren’t being accidentally influenced by it.

## commands

    - Running Only One Test

        pytest test_validator.py::test_regular_email_validates

    - Exit on first error

        pytest -x

    - Run the last failed test only

        pytest --lf

    - Run all tests, but run the last failed ones first

        pytest --ff

    - Show values of local variables in the output

        pytest -l

    - Using pytest with a debugger

        pytest --lf --trace

# conftest.py

    - Each folder containing test files can contain a conftest.py file which is read by pytest.
    - This is a good place to place your custom fixtures into as these could be shared between different test files.
