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
