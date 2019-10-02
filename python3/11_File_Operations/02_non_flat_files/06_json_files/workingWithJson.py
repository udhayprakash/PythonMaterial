#!/usr/bin/python
import json
from pprint import pprint

book = {}
book['title'] = 'Python Programming Essentials'
book['tags'] = ('Python', 'Programming')
book['published'] = True
book['comment_link'] = None
book['author'] = 'Udhay'
book['id'] = 786

print('\nbook details :\n', book)
print("type(book) is ", type(book))
pprint(book)

# Serilazation
with open('ebook.json', 'w') as f:
    json.dump(book, f)
    f.close()

# De-serialization
print('\ndeserializing the json data \n')
with open('ebook.json', 'rb') as g:
    data = json.load(g)
    g.close()

print("data = ", data)

print('\nprinting using pretty print')
import pprint

pprint.pprint(data)
pprint.pprint(data, indent=4)

# Assignemnt ; try to work with json.load and json.dumps- json.loads
