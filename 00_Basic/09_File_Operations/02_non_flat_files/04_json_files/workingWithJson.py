#!/usr/bin/python

#import simplejson

try:
	import simplejson as json
except ImportError, ex:
	print "The error  is \t", ex
	print 'importing json module'
	import json

book = {}
book['title'] = 'Python Programming Essentials'
book['tags'] = ('Python', 'Programming')
book['published'] = True
book['comment_link'] = None
book['author'] = 'Udhay'
book['id'] = 786

print '\nbook details :\n', book
print "type(book) is ", type(book)
# Serilazation
with open('ebook.json',  'wb') as f:
	json.dump(book, f)

# De-serialization
print '\ndeserializing the json data \n'
with open('ebook.json', 'rb') as g:
  data = json.load(g)
  g.close()

print "data = ", data

print '\nprinting using pretty print'
import pprint
pprint.pprint(data)
pprint.pprint(data, indent = 4)
import os
import sys
if sys.platform == 'win32':
    os.system('type ebook.json')  # linux - cat ; windows - type
else:
    os.system("cat ebook.json")

# Assignemnt ; try to work with json.load and json.dumps- json.loads