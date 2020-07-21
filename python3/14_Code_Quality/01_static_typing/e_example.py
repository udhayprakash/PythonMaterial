# =========================
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


def mirror(name: Any) -> str:
    return str(name)


print(mirror(100))
print(mirror(123.453))
print(mirror(True))
print(mirror(None))
