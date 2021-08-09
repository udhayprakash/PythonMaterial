#!/usr/bin/python
"""
Purpose:
    pip install parse
"""

import parse

result = parse.parse(
    '{greeting}, the time is {now:tt}',
    'Hello, the time is 6:30 PM'
)
print(result)

print(result.named['greeting'])
