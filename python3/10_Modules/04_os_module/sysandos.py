import os
import sys

print("Command line arguments received were:")
for arg in enumerate(sys.argv):
    print(f"Argument {arg[0]} is {arg[1]!r}.")

print("\nFinding out some information about Python environment.")

print(f"Current Python version is {sys.hexversion}.")
print(f"Current implementation is {sys.implementation}.")
print(f"Recursion limit is {sys.getrecursionlimit()} levels.")
fi = sys.float_info
print(f"For float values, maximum exponent is {fi.max_exp}.")
print(f"For float values, mantissa contains {fi.mant_dig} bits.")


# The module os allows us to access the file system. Let's take a look
# around the current directory and find all the .txt files inside it.

print("\nMoving on to os functionality...")
names = os.listdir(".")
print(f"The current directory contains {len(names)} filenames.")
for name in names:
    if os.path.isfile(name) and name.endswith(".txt"):
        st = os.stat(name)  # an os.statresult object
        print(f"Found text file {name} of {st.st_size} bytes.")
        print(f"This file was last modified at time {st.st_mtime}.")
