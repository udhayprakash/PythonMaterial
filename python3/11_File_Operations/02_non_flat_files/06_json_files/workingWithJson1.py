#!/usr/bin/python

# workingWithJson.py

'''
    Purpose: Demonstrate usage of json
'''
# official website http://json.org/

# Dictionary to Json

import json

student = {"101": {"result": True, "class": 'V', "Name": 'Rohit', "Roll_no": 7},
           "102": {"result": True, "class": 'V', "Name": 'David', "Roll_no": 8},
           "103": {"result": False, "class": 'V', "Name": 'Samiya', "Roll_no": 12}}
print(json.dumps(student))

print '-' * 100
# Python Dictionaries to JSON strings (sorted by key)
import json

student = {"101": {"class": 'V', "Name": 'Rohit', "Roll_no": 7},
           "102": {"class": 'V', "Name": 'David', "Roll_no": 8},
           "103": {"class": 'V', "Name": 'Samiya', "Roll_no": 12}}
print(json.dumps(student, sort_keys=True))

# Json stores the data in the order inputted.
print '-' * 100
# Python tuple to JSON array
import json

tup1 = 'Red', 'Black', 'White'
print(json.dumps(tup1));

print '-' * 100
# Python string to JSON string
import json

string1 = 'Python and JSON';
print(json.dumps(string1));

print '-' * 100
# Python Boolean values to JSON Boolean values
import json

x = True;
print(json.dumps(x));

print '-' * 100

# Python int, float, int- & float-derived Enums to JSON number
x = -456;
y = -1.406;
z = 2.12e-10
print(json.dumps(x));
print(json.dumps(y));
print(json.dumps(z));

print '-' * 100
print 'DECODING THE JSON'
print '-' * 100
'''
json to python object conversion pairs:
JSON	        Python
----------------------
object	        dict
array	        list
string	        str
number(int)	    int
number(real)	float
true	        True
false	        False
null	        None

'''

# JSON strings to Python Dictionaries
import json

json_data = '{"103": {"class": "V", "Name": "Samiya", "Roll_n": 12}, "102": {"class": "V", "Name": "David", "Roll_no": 8}, "101": {"class": "V", "Name": "Rohit", "Roll_no": 7}}';
print(json.loads(json_data));

print '-' * 100

# JSON array Python tuple
Json_array = ["Red", "Black", "White"]
print(json.dumps(Json_array));

# Python list to JSON array
list1 = [5, 12, 13, 14];
print(json.dumps(list1));

# JSON string to Python string
Json_string = "Python and JSON"
print(json.dumps(Json_string));

print '+' * 100
print '+' * 100

import json

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print json.dumps('\"foo\bar')

print json.dumps(u'\u1234')

print json.dumps('\\')

print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

data = json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
print data

# pretty printing
print json.dumps({'4': 5, '6': 7}, sort_keys=True,
                 indent=4, separators=(',', ': '))
