import os, os.path
import re

# This is the first implementation
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if re.search (r".*\.pdf", path):
         print path


# This is the second implementation, which skips
# files with spaces in their names.
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if not re.search (r".*\.pdf", path): continue
      if re.search (r" ", path): continue

      print path


# This is the third implementation, which
# skips over files that have the letter ".hu" in the path.
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if not re.search (r".*\.pdf", path): continue
      if re.search (r".\.hu", path): continue

      print path

os.path.walk ('.', print_pdf, 0)

# This will default to the last definition in the file
os.path.walk ('.', print_pdf, 0)

