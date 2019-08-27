print('Hello world')

# aspect oriented programming
num1 = 123
num2 = 345

result = num1 + num2 
print(result)


# functional oriented programming
def addition(n1, n2):
    return n1 + n2

r1 = addition(num1, num2)
print(r1)


# Object Oriented 

class AdditionClass:
    def __init__(self, _n1, _n2):
        self.n1 = _n1 
        self.n2 = _n2 

    def add(self):
        return self.n1 + self.n2 

r2 = AdditionClass(num1, num2)
print(r2.add())