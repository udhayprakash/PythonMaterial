"""
Purpose: Static typing with mypy

"""


# Method 1 : Traditional approach
def hello(name):
    return f"Hello {name}"


result = hello("Python")
print(result)


# -------------------------------
# Method 2 : Adding Typing
def hello2(name: str) -> str:
    return f"Hello {name}"


result = hello2("Python")
print(result)
