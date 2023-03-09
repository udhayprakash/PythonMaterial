print("Hello world")

# calculator - addition

# Method 1 - aspect-oriented programming
num1 = 100
num2 = 200

add_res = num1 + num2
print(add_res)


# Method 2 - function-oriented programming
def addition(n1, n2):
    return n1 + n2


add_res = addition(num1, num2)
print(add_res)


# Method 3 -  Object Oriented Programming
class Calculator:
    def __init__(self, v1, v2) -> None:
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2


cl = Calculator(num1, num2)
add_res = cl.add()
print(add_res)


# -----------------------
name = "Hari Krishna"
print(name)
print(name.upper())
print(name.lower())

print("Hari" in name)

# string reversal
print(name[::-1])  # anhsirK iraH
