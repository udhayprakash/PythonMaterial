"""
Purpose: Exception Groups
    introduced in Python 3.11

"""

try:
    raise ExceptionGroup(
        "eg",
        [
            ValueError(1),
            TypeError(2),
            OSError(3),
            ExceptionGroup("nested", [OSError(4), TypeError(5), ValueError(6)]),
        ],
    )
except ValueError as ex:
    print(f"{ex =}")
