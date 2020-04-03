#!/usr/bin/python
"""
Purpose: Static Typing in python
    http://mypy-lang.org
python -m pip install -U mypy

python -m mypy filename.py
"""
import typing

for ech_attr in dir(typing):
    print(ech_attr)
