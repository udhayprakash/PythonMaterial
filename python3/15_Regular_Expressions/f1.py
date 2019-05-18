#!/usr/bin/python

import re

string = "we had class on regular expressions\nThis is a python class.\nThe class is at 10pm IST"
print(string)

#reg = re.compile("This")
#reg = re.compile("^This")
reg = re.compile("^This",re.M)
#print "compiled regex object is ", reg




print("working on ^ - beginning with")
print("The matched string is %s" %(reg.match(string)))

print("The searched string is %s" %(reg.search(string)))
print( reg.search(string).group())

print("working on $ - ending with")
regObject = re.compile("expressions$",re.M)
print(regObject.match(string))
print(regObject.search(string))


# ^
# $
# re.M or re.MULTILINE
