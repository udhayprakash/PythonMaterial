#!/usr/bin/python

import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

print(yaml.dump(users))


my_dict = {
    'a': 1,
    'b': True,
    'c': False,
    'd': None
}

# python object to yaml
yaml_string1 = yaml.dump(my_dict)
print(type(yaml_string1), yaml_string1)
