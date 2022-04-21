#!/usr/bin/python
"""
Purpose: Inverting a dictionary
"""
from collections import defaultdict
import json


def tree():
    """
    factory that creates  a defaultdict that also uses this factory
    """
    return defaultdict(tree)


root = tree()

root["page 1"]["row 1"]["content"] = "This is line ONE"
root["page 1"]["row 2"]["content"] = "This is line TWO"
root["page 2"]["titlw"] = "This is page 2"

print(json.dumps(root, indent=4))
"""
{
    "page 1": {
        "row 1": {
            "content": "This is line ONE"
        },
        "row 2": {
            "content": "This is line TWO"
        }
    },
    "page 2": {
        "titlw": "This is page 2"
    }
}
"""
