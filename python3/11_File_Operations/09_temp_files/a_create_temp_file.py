#!/usr/bin/python
"""
Purpose: creating temp files
"""
import os
import tempfile

# print(dir(tempfile))
print("Current temp directory:", tempfile.gettempdir())

tempfile.tempdir = os.path.join(os.path.dirname(__file__), "temp")
if not os.path.exists(tempfile.tempdir):
    os.mkdir(tempfile.tempdir)

print("Temp directory after change:", tempfile.gettempdir())


fh = tempfile.TemporaryFile()
fh.write(b"Hello world!")

fh.seek(0)

existing_content = fh.read()
print(existing_content)

fh.close()


with tempfile.TemporaryFile() as fp:
    fp.write(b"Hello world!")

    fp.seek(0)

    existing_content = fp.read()
    print(existing_content)

    fp.close()


with tempfile.TemporaryDirectory() as tmpdirname:
    print("created temporary directory", tmpdirname)

print()

# creating Named temporary files
f = tempfile.NamedTemporaryFile(delete=False)
print(f"{f.name=}")
print(f"{f.file=}")

f.write(b"Hello World!\n")
f.close()

print(f"Before - is file present: {os.path.exists(f.name)}")

os.unlink(f.name)  # or os.remove(f.name)

print(f"After - is file present : {os.path.exists(f.name)}")
print()

# Adding prefix and suffix to named temp files
f = tempfile.NamedTemporaryFile(prefix="dummyPrefix_", suffix="_dummySuffix")
print(f"{f.name=}")
print(f"{f.file=}")

print(f"Before - is file present: {os.path.exists(f.name)}")
os.unlink(f.name)
print(f"After - is file present : {os.path.exists(f.name)}")
