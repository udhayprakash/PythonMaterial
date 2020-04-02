print('Hello world')

# calculator

# Method 1: aspect-oriented programming 
num1 = 100
num2 = 200

result = num1 + num2 
print(result)


# Method 2: functional Oriented
def addition(n1, n2):
    r1 = n1 + n2 
    return r1

print(addition(num1, num2))


# Method 3: Object Oriented Programming
class Arithmetic:
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def add(self):
        return self.num1 + self.num2

a = Arithmetic(num1, num2)
print(a.add())


# -----------------------
name = 'Varun Piyush'
print(name)
print(name[::-1])
print(name.lower())
print(name.upper())

print(name.islower())
