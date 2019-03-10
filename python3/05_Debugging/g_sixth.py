#!/usr/bin/python
# sixth.py
import pdb

def fourth():
  second()
  print "this is my fourth function \n"
def third():
  print "this is my third function \n"
def second():
  third()
  print "this is my second function \n"
def first():
  fourth()
  print "this is my first function \n"

pdb.set_trace()
first()
