"""
Purpose: Exception Groups
    introduced in Python 3.11

PEP 654 - Exception Groups and except*

"""
print("\n CASE 1")
try:
    raise ValueError("This is Value Error")
except ValueError as ex:
    print(f"{ex =}")

print("\n CASE 2")
try:
    raise ExceptionGroup(
        "It can both Value & Type Errors",
        [
            ValueError(1),
            TypeError(2),
        ],
    )
except ValueError as ve:
    print(f"Value Error: {ve =}")
except TypeError as te:
    print(f"Type Error: {te =}")
except Exception as ex:
    print(f"UnHandled Exception: {ex =}")

# NOTE: ExceptionGroup cant be handled by individual exception types

print("\n CASE 3")
try:
    raise ExceptionGroup(
        "It can both Value & Type Errors",
        [
            ValueError(1),
            TypeError(2),
        ],
    )
except* ValueError as ve:
    print(f"Value Error: {ve =}")
except* TypeError as te:
    print(f"Type Error: {te =}")
except* Exception as ex:
    print(f"UnHandled Exception: {ex =}")

# NOTE: except* & except CANT BE used within same try-except blocks


print("\n CASE 4")
try:
    raise ExceptionGroup(
        "It can both Value & Type Errors",
        [
            ValueError(1),
            TypeError(2),
            OSError(3),  # Added New Exception
        ],
    )
except* ValueError as ve:
    print(f"Value Error: {ve =}")
except* TypeError as te:
    print(f"Type Error: {te =}")
except* Exception as ex:
    print(f"UnHandled Exception: {ex =}")

print("\n CASE 5")
try:
    raise ExceptionGroup(
        "It can both Value & Type Errors",
        [
            ValueError(1),
            TypeError(2),
            OSError(3),  # Added New Exception
            ExceptionGroup(
                "Another group",  # Second group inside main group
                [Exception("Another error")],
            ),
        ],
    )
except* ValueError as ve:
    print(f"Value Error: {ve =}")
except* TypeError as te:
    print(f"Type Error: {te =}")
except* Exception as ex:
    print(f"UnHandled Exception: {ex =}")


print("\n CASE 6")
try:
    raise ExceptionGroup(
        "It can both Value & Type Errors",
        [
            ValueError(1),
            TypeError(2),
            OSError(3),  # Added New Exception
            ExceptionGroup(
                "Another group",  # Second group inside main group
                [Exception("Another error")],
            ),
            ExceptionGroup("nested", [OSError(4), TypeError(5), ValueError(6)]),
        ],
    )
except* ValueError as ve:
    print(f"Value Error: {ve =}")
except* TypeError as te:
    print(f"Type Error: {te =}")
except* Exception as ex:
    print(f"UnHandled Exception: {ex =}")
    try:
        ex_subgroup = ex.subgroup(1)
        # this call will throw error, if exception in subgroup
    except* Exception as sub_ex:
        print(f"\tSubGroup Error {sub_ex =}")


print("\n CASE 7")
try:
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
    except* ValueError as e:
        print(f"*ValueError: {e!r}")
        raise
    except* OSError as e:
        print(f"*OSError: {e!r}")
except ExceptionGroup as e:
    print(repr(e))
