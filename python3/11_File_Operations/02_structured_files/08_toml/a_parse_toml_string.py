"""
Purpose: Parsing TOML string

    In python 3.11, tomllib module is added to builtin modules
"""
import tomllib

toml_str = """
[build]
python-version = "3.11.0"
python-implementation = "CPython"

[tool.poetry.dev-dependencies]
tryceratops = "^1.1.0"
"""

data = tomllib.loads(toml_str)
print(data)
