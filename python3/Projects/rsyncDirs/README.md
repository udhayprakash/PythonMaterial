# RSync Two Dirs

This script is responsible for syncing files, uniderectionally, from source directory to the destination directory.

## Installation

Python installation, followed by PYTHON_PATH setup needed, as prerequisite.

## Demo

To run the script in DRY_RUN mode,

    python rsync.py -dr

To run the script in EXECUTION mode,

    python rsync.py

## Running Tests

To run tests, run the following command

```python
  python test_rsync.py
```

To get the code coverage,

```python
  python -m coverage run test_rsync.py
```
