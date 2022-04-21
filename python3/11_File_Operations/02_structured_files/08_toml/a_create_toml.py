#!/usr/bin/python3
"""
Purpose: TOML - Tom's Obvious, Minimal Language.


    https://toml.io/en/
    https://github.com/toml-lang/toml

pip install toml

"""
import toml

print(dir(toml))
print()

# toml file to python dict
with open('sample.toml', 'r') as fh:
    parsed_toml_dict = toml.load(fh)
    print(parsed_toml_dict)

print()
# python dict to toml string
toml_string = toml.dumps(parsed_toml_dict)
print(toml_string)

print()
# python dict to toml file
with open('new_file.toml', 'w') as fh:
    toml.dump(parsed_toml_dict, fh)
