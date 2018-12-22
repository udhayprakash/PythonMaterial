import os, os.path
import re
from stat import *

# This is the first instance. Use this alone for the first invocation
# of test_find.py
def find (where='.*', content=None, start='.', ext=None, logic=None):
    return ([])

# This is the second instance. It adds more features, but does not
# pass all the tests.
def find (where='.*', content=None, start='.', ext=None, logic=None):
   context = {}
   context['where'] = where
   context['content'] = content
   context['return'] = []

   os.path.walk (start, find_file, context)

   return context['return']

def find_file (context, dir, files):
   for file in files:
      # Find out things about this file.
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      try:
         ext = os.path.splitext (file)[1][1:]
      except:
         ext = ''
      stat = os.stat(path)
      size = stat[ST_SIZE]

      # Don't treat directories like files
      if S_ISDIR(stat[ST_MODE]): continue

      # Do filtration based on the original parameters of find()
      if not re.search (context['where'], file): continue

      # Do content filtration last, to avoid it as much as possible
      if context['content']:
         f = open (path, 'r')
         match = 0
         for l in f.readlines():
            if re.search(context['content'], l):
               match = 1
               break
         f.close()
         if not match: continue

      # Build the return value for any files that passed the filtration tests.
      file_return = (path, file, ext, size)
      context['return'].append (file_return)


# This is the third implementation which adds more funcationality. This passes
# all of the test conditions in the test_find.py.

def find (where='.*', content=None, start='.', ext=None, logic=None):
   context = {}
   context['where'] = where
   context['content'] = content
   context['return'] = []
   context['ext'] = ext
   context['logic'] = logic

   os.path.walk (start, find_file, context)

   return context['return']

def find_file (context, dir, files):
   for file in files:
      # Find out things about this file.
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      try:
         ext = os.path.splitext (file)[1][1:]
      except:
         ext = ''
      stat = os.stat(path)
      size = stat[ST_SIZE]

      # Don't treat directories like files
      if S_ISDIR(stat[ST_MODE]): continue

      # Do filtration based on the original parameters of find()
      if not re.search (context['where'], file): continue
      if context['ext']:
         if ext != context['ext']: continue
      if context['logic']:
         arg = {}
         arg['path'] = path
         arg['ext'] = ext
         arg['stat'] = stat
         arg['size'] = size
         arg['mod'] = stat[ST_MTIME]

         if not context['logic'](arg): continue

      # Do content filtration last, to avoid it as much as possible
      if context['content']:
         f = open (path, 'r')
         match = 0
         for l in f.readlines():
            if re.search(context['content'], l):
               match = 1
               break
         f.close()
         if not match: continue

      # Build the return value for any files that passed the filtration tests.
      file_return = (path, file, ext, size)
      context['return'].append (file_return)
