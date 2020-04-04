#!/usr/bin/python
import re
import sys

reg = re.compile('yes', re.I)

answer = input("do you want to continue the game:")
if reg.match(answer):
    print("Thanks for choosing to continue with the game")
else:
    print("you have no taste!!!")
    sys.exit()
