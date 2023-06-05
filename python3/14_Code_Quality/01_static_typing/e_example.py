# Method 1 : Traditional Approach
def mirror(name):
    return str(name)


print(mirror(100))
print(mirror(123.453))
print(mirror(True))
print(mirror(None))

# ----------------------------
# Method 2: Adding typing
from typing import Any


def mirror2(name: Any) -> str:
    return str(name)


print(mirror2(100))
print(mirror2(123.453))
print(mirror2(True))
print(mirror2(None))
