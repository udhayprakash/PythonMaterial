import json
import sys

import yaml

"""
Example usage:

$ python json_to_yaml.py json_test.json
"""

if len(sys.argv) != 2:
    print(len(sys.argv))
    print("USAGE\n$ python json_to_yaml.py json_test.json")
    sys.exit(1)

# load json data
json_data = json.loads(open(sys.argv[1]).read())

# convert unicode to string
converted_json_data = json.dumps(json_data)

# output yaml
print(
    yaml.dump(
        yaml.load(converted_json_data, Loader=yaml.FullLoader), default_flow_style=False
    )
)
