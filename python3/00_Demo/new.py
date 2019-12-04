print('hello world')

# aspect oriented programming
num1 = 123
num2 = 345

num3 = num1 + num2
print(num3)


# functional oriented programming
def addition(n1, n2):
    result = n1 + n2
    return result


print(addition(num1, num2))


# Object oriented programming
class Addition:
    def __init__(self, nm1, nm2):
        self.n1 = nm1
        self.n2 = nm2

    def add(self):
        return self.n1 + self.n2


r2 = Addition(num1, num2)
print(r2.add())
