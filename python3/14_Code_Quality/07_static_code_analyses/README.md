## Static Code Analyses

- Provides insight into code without executing it
- Executes quickly in comparison with dynamic analysis
- Can automate code quality maintenance
- Can automate the search for bugs at the early stages (although not all).
- Can automate the finding of security problems at an early stage
- Tools
  1. Pylint
  2. Pyflakes
  3. Mypy
  4. Prospector
  5. bandit - secure coding (SQL injections) analyses

### pylint codes

```
    -------------------------------------------------------------------------
    Message Object    Expansion       Explanation
    -------------------------------------------------------------------------
        C               Convention      Displayed when the program
                                        is not following the standard rules.
        R               Refactor        Displayed for bad code smell
        W               Warning         Displayed for python specific problems
        E               Error           Displayed when that particular line
                                        execution results some error
        F               Fatal           Displayed when pylint has no access to
                                        further process that line.
    -------------------------------------------------------------------------
```

- black : auto-formats Python files in place.
- docformatter : auto-formats docstrings.
- flake8 : a linter that enforces Python style guides
- pylint : another linter for Python.
- mypy : adds static type checks to Python code, needs code to include type hints for it to work.
- isort : sorts imports alphabetically.
- bandit : finds common security issues in Python code.

- pep8
  pip install pep8
  pep8 filename.py

- autopep8
  pip install autopep8
  autopep8 --in-place filename.py

pip install pytest-cov
py.test test_calculate.py
coverage run -m
