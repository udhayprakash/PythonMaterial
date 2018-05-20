import sys
import json
import yaml

"""
Example usage:

$ python json_to_yaml.py json_test.json
"""

if len(sys.argv) != 3:
    print "USAGE"
    print "$ python json_to_yaml.py json_test.json"
    sys.exit(1)
    
# load json data
json_data = json.loads(open(sys.argv[1]).read())
# convert unicode to string
converted_json_data = json.dumps(json_data)
# output yaml
print(yaml.dump(yaml.load(converted_json_data), default_flow_style=False))
