#!/usr/bin/python
"""
Purpose:
    Use the NewType() helper function to create
    distinct types:
"""
from typing import NewType

UserId = NewType("UserId", int)
some_id = UserId(524313)

print(f"type(some_id):{type(some_id)}")
print(f"some_id      :{some_id}")
