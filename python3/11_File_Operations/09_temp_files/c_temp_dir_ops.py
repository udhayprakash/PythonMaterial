import os
import tempfile

# Changing temp directory path
tempfile.tempdir = os.path.join(os.path.dirname(__file__), "temp")
if not os.path.exists(tempfile.tempdir):
    os.mkdir(tempfile.tempdir)


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

# Either specifically delete file, or mark delete-True to delete
os.unlink(f.name)  # or os.remove(f.name)

print(f"After - is file present : {os.path.exists(f.name)}")
print()

# Adding prefix and suffix to named temp files
with tempfile.NamedTemporaryFile(prefix="dummyPrefix_", suffix="_dummySuffix") as f:
    print(f"{f.name=}")
    print(f"{f.file=}")

    f.write(b"Hello World2222!\n")

    print(f"Before - is file present: {os.path.exists(f.name)}")
    os.unlink(f.name)
    print(f"After - is file present : {os.path.exists(f.name)}")
