#!/usr/bin/python3
"""
Purpose: Dictionaries
"""
from pprint import pprint

language = dict()

# add new keys
language['name'] = 'Python'
language['creator'] = 'Gudo Van Russum'

pprint(language)
print()

# add single key value pair
language['latest_version'] = '2.7.16'
pprint(language)

# Add more key-value pair in bulk
python_dict = {
    'name': 'Python',
    'maintainer': 'Almighty',
    'latest_version': '3.8.5',
    'dev_version': '3.9'
}
pprint(python_dict)


# Dictionary concatenation
# language + python_dict # is not possible with +

print('\n After update')
language.update(python_dict)
# NOTE:
# 1. first dictionary is modified, and not the second one
# 2. If keys are present, values will be updates,
#  else new key-values pairs will be created

pprint(language)
pprint(python_dict)
print()

python_dict.update({
    'dev_version': '3.9.0rc'
})
pprint(python_dict)


# For deleting key-value pairs
# print(f"{python_dict.pop() =}")
# TypeError: pop expected at least 1 argument, got 0
print(f"{python_dict.pop('maintainer') =}")
print(python_dict)

try:
    print(f"{python_dict.pop('maintainer') =}")
except KeyError as ex:
    print('no such key', ex)

print(f"{python_dict.pop('maintainer', None) =}")
print(f"{python_dict.pop('maintainer', 'no such key') =}")
print(python_dict)

# last key-value pair will be deleted
print()
print(f"{python_dict.popitem() =}")
print(f"{python_dict.popitem() =}")
print(python_dict)


del python_dict['name']
print(python_dict)

del python_dict
# print(python_dict)  NameError: name 'python_dict' is not defined

# Question: del dict['key'] vs dict.pop('key')
