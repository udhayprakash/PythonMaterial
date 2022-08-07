import toml

toml_str = """
[[players]]
name = "Lehtinen"
number = 26

[[players]]
name = "Numminen"
number = 27
"""

toml_dict = toml.loads(toml_str)
assert toml_dict == {
    "players": [{"name": "Lehtinen", "number": 26}, {"name": "Numminen", "number": 27}]
}


with open("sample.toml", "r") as f:
    toml_dict = toml.load(f)

print(toml_dict)

# === Handle invalid TOML
try:
    toml_dict = toml.loads("]] this is invalid TOML [[")
except toml.TomlDecodeError:
    print("Yep, definitely not valid.")
