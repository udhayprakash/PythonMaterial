#!/usr/bin/python3
"""
Purpose: creating temp files
"""
import os
import tempfile

# print(dir(tempfile))

# 1. Changing the TEMP directory path

print("Current temp directory     :", tempfile.gettempdir())

tempfile.tempdir = os.path.join(os.path.dirname(__file__), "temp")
# It doesnt validate the presence of directory given
print("Temp directory after change:", tempfile.gettempdir())

if not os.path.exists(tempfile.tempdir):
    os.mkdir(tempfile.tempdir)


# 2. File Operations with TEMP files

# 2a. Creating temp file
fh = tempfile.TemporaryFile()

# 2b. write content in created temp file
fh.write(b"Hello world!")

# 2c. Reading content from temp file
fh.seek(0)  # moving cursor to 0th position, to read from there
existing_content = fh.read()
print(existing_content)

fh.close()


# Alternatively, with context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b"Hello world!")

    fp.seek(0)

    existing_content = fp.read()
    print(existing_content)

    fp.close()
