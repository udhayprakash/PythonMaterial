"""
Purpose: Secure means it will ensure
    that created temp files were deleted, after servng purpose.
"""
import os
import tempfile

# mkstemp is responsible for deleting the temporary file when done with it
fd, path = tempfile.mkstemp(
    prefix="MyTemp_", suffix="_File", dir=tempfile.gettempdir(), text=True
)
print(f"{fd =} {path =}")
print(os.path.exists(path))  # True
print()

fd, path = tempfile.mkstemp(text=True)
print(f"{fd =} {path =}")
try:
    with os.fdopen(fd, "w") as tmp:
        tmp.write("stuff")
finally:
    os.remove(path)

print(os.path.exists(path))  # False
print()

fd, path = tempfile.mkstemp(text=True, suffix="_File")
print(f"{fd =} {path =}")
