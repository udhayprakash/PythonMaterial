#!/usr/bin/python
# Author : santosh D
# Usage : How to re-try with entering the values after exceptions in python.
# 

def my_input():
  my_num1 = int(raw_input("please enter the num1:"))
  my_num2 = int(raw_input("please enter the num2:"))
  return my_num1,my_num2

while True:
  try:
    (a,b)=my_input()
  except ValueError:
    continue
  else:
    print a,b
    break
