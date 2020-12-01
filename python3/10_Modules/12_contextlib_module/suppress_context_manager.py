import os
from contextlib import suppress

try:
    os.remove('file.txt')
except FileNotFoundError:
    pass


with suppress(FileNotFoundError):
    os.remove('file.txt')