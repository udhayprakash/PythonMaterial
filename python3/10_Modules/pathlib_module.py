#!/usr/bin/python
"""
Purpose: pathlib module usage
"""
# import pathlib
# print(dir(pathlib))
# ['EBADF', 'EINVAL', 'ELOOP', 'ENOENT', 'ENOTDIR', 'Path', 'PosixPath',
# 'PurePath', 'PurePosixPath', 'PureWindowsPath', 'S_ISBLK', 'S_ISCHR',
# 'S_ISDIR', 'S_ISFIFO', 'S_ISLNK', 'S_ISREG', 'S_ISSOCK', 'Sequence',
#  'WindowsPath', '_Accessor', '_Flavour', '_IGNORED_ERROS', '_IGNORED_WINERRORS',
#  '_NormalAccessor', '_PathParents', '_PosixFlavour', '_PreciseSelector',
#   '_RecursiveWildcardSelector', '_Selector', '_TerminatingSelector',
#   '_WildcardSelector', '_WindowsFlavour', '__all__','__builtins__',
#   '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__spec__', '_getfinalpathname', '_ignore_error',
#   '_is_wildcard_pattern', '_make_selector', '_normal_accessor', '_posix_flavour',
#    '_windows_flavour', 'attrgetter', 'fnmatch', 'functools', 'io', 'nt', 'ntpath',
#     'os', 'posixpath', 're', 'supports_symlinks', 'sys', 'urlquote_from_bytes']

from pathlib import Path
import os

print(f"Current directory: {Path.cwd()}")
print(f"Home directory   : {Path.home()}")
print()

# Change directory
path = Path('..')
print(f"Current directory: {Path.cwd()}")

os.chdir(path)
print(f"Current directory: {Path.cwd()}")

os.chdir('..')
print(f"Current directory: {Path.cwd()}")

print()

# Create paths

# Constructing the paths
wave = Path("ocean", "wave.txt")
print(wave)                 # ocean\wave.txt

home = Path.home()
wave_absolute = Path(home, "ocean", "wave.txt")
print(home)                 # C:\Users\Amma
print(wave_absolute)        # C:\Users\Amma\ocean\wave.txt


shark = Path(Path.home(), "ocean", "animals", Path("fish", "shark.txt"))
print(shark)                # C:\Users\Amma\ocean\animals\fish\shark.txt

# Accessing file attributes
wave = Path("ocean", "wave.txt")
print(wave)                 # ocean\wave.txt
print(wave.name)            # wave.txt
print(wave.suffix)          # .txt

wave = Path("ocean", "wave.txt")
tides = wave.with_name("tides.txt")
print(wave)                 # ocean\wave.txt
print(tides)                # ocean\tides.txt

# Accessing Ancestors - parent dirs
shark = Path("ocean", "animals", "fish", "shark.txt")
print(shark)                # ocean\animals\fish\shark.txt
print(shark.parent)         # ocean\animals\fish
print(shark.parent.parent)  # ocean\animals
print()

# Computing Relative Paths
shark = Path("ocean", "animals", "fish", "shark.txt")
below_ocean = shark.relative_to(Path("ocean"))
below_animals = shark.relative_to(Path("ocean", "animals"))
print(shark)                # ocean\animals\fish\shark.txt
print(below_ocean)          # animals\fish\shark.txt
print(below_animals)        # fish\shark.txt
