## Static Code Analyzers

- pycodestyle
  - https://pypi.org/project/pycodestyle/
  - Checks if your code follows PEP8
- Pylint
  - https://www.pylint.org/
  - An in-depth static code testing tool that finds common issues with code
- PyFlakes
  - https://pypi.org/project/pyflakes/
  - Another static code testing tool for Python
- flake8

  - https://pypi.org/project/flake8/
  - A wrapper around PyFlakes, pycodestyle and a McCabe script
  - .flake8 stores the configuration
  - a linter to enforce coding style

- Black

  - https://black.readthedocs.io/en/stable/
  - A code formatter that mostly follows PEP8
  - The tool.black section of the pyproject.toml stores the configuration

- bandit

  - linter to check for security vulnerabilities
  - The bandit section of the .pre-commit-config.yaml stores the configuration

- isort

  - an automatic import formatter
  - .isort.cfg stores the configuration

- seed-isort-config
  - a tool to statically populate the known_third_party part of the .isort.cfg

pre-commit installs and manages the environments for the code linting and formatting tools

- For installing pre-commit hook to the project repo,

  pre-commit install

- For running the pre-commit hook, before commiting the code,

  pre-commit run --all-files
