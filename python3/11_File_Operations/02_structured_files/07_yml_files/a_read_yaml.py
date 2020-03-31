#!/usr/bin/python
"""
Purpose: Reading (Parsing) YAML files
    YAML
        - YAML Ain't Markup Language
        - human-readable data-serialization language.
        - commonly used for configuration files,
        - also, in data storage (e.g. debugging output) or transmittion (e.g. document headers)

        - natively supports three basic data types:
            1. scalars (such as strings, integers, and floats),
            2. lists, and
            3. associative arrays.

    Installation
        pip install pyyaml
"""
from pprint import pprint

import yaml

# scalar values to python dictionary
with open('items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    pprint(data)

    f.close()
