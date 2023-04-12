print("Hello world")

# Method 1 - aspect-oriented programming
num1 = 100
num2 = 200
add_result = num1 + num2
print(add_result)
print()


# Method 2 - function-oriented programming
def addition(num1, num2):
    return num1 + num2


add_result = addition(num1, num2)
print(add_result)

print(addition(10, 20))
print(addition(100, 200))
print(addition(34, 20))
print()


# Method 3 -  Object Oriented Programming
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2


cal1 = Calculator(10, 20)
add_result = cal1.addition()
print(add_result)

cal2 = Calculator(100, 200)
print(cal2.addition())
print(cal2.subtraction())
print(cal2.multiplication())
print(cal2.addition())
