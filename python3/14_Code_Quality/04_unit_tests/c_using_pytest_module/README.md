Pytest - most popular python package for testing - basis for rich ecosystem of testing plugins and extensions - Not unittest - Need to install
pip install -U pytest

        ~pytest --version
         pytest 6.0.0
    - pytest will run all files of the form test_*.py or *_test.py in
      the current directory and its subdirectories.
    - pytest provides Builtin fixtures/function arguments to request arbitrary resources, like a unique temporary directory:
    - commands
        pytest --version # shows where pytest was imported from
        pytest --fixtures # show available builtin function arguments
        pytest -h | --help # show help on command line and config file options

    - Running pytest can result in six different exit codes:
        Exit code 0 All tests were collected and passed successfully
        Exit code 1 Tests were collected and run but some of the tests failed
        Exit code 2 Test execution was interrupted by the user
        Exit code 3 Internal error happened while executing tests
        Exit code 4 pytest command line usage error
        Exit code 5 No tests were collected

    - To stop the testing process after the first (N) failures:
        pytest -x # stop after first failure
        pytest --maxfail=2 # stop after two failures
