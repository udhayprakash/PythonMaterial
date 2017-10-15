#!/usr/bin/python

class InvalidAge(Exception):
  def __init__(self,age):
    self.age = age

def validate_age(age):
  if age < 18:
    raise InvalidAge(age)
    

# Main
   
age = int(raw_input("please enter your age:"))
try:
  validate_age(age)
except Exception as e:
  print "buddy!!! you are still young {}".format(e.age)
else:
  print "how many tickets you need"


