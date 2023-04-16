"""
Purpose: Python is a dynamic Typed Language.
    Progamming Languages
        - Classficiation
            1. Static-Typed Languages
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            2. Dynamic Typed Languages
                 - create when you need. No declaration needed
                    num1 = 123
"""
num1 = 100

type(num1)
print(type(num1))

print(num1)
print("num1")

print("num1", num1)
print("num1 =", num1)

print("num1 =", num1, "type =", type(num1))

# Python is a dynamic-typed language
num1 = 300
print("num1 =", num1, "type =", type(num1))  # int

num1 = 300.0
print("num1 =", num1, "type =", type(num1))  # float

num1 = (300,)
print("num1 =", num1, "type =", type(num1))  # tuple
print()

num1 = 300.0
print("num1 =", num1, "type =", type(num1))  # float

num1 = -0.09
print("num1 =", num1, "type =", type(num1))  # float

num1 = -0.09j
print("num1 =", num1, "type =", type(num1))  # complex
print()

num1 = "300"
print("num1 =", num1, "type =", type(num1))  # string

num1 = "three"
print("num1 =", num1, "type =", type(num1))  # string
print()

num1 = True
# num1 = true  # PYTHON IS A CASE-SENSITIVE LANGUAGE
print("num1 =", num1, "type =", type(num1))  # bool

num1 = False
print("num1 =", num1, "type =", type(num1))  # bool

num1 = None
print("num1 =", num1, "type =", type(num1))  # none

num1 = "NONE"
print("num1 =", num1, "type =", type(num1))  # string

num1 = "none"
print("num1 =", num1, "type =", type(num1))  # string

# NOTE: Strings need to be declared in quotes
