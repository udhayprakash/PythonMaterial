"""
Purpose: newly style classes better support property decorator

To access a method as a variable, we need property decorator

"""


class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property  # .getter
    def full_name(self):
        return self.first + " " + self.last

    @full_name.setter
    def full_name(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname


person1 = Person("Udhay", "Prakash")
print(person1.email())

print(f"person1.first      :{person1.first}")
print(f"person1.last       :{person1.last}")
print(f"person1.full_name  :{person1.full_name}")
print()

# Updating the value
person1.full_name = "Shyam Benegal"
print(f"person1.first      :{person1.first}")
print(f"person1.last       :{person1.last}")
print(f"person1.full_name  :{person1.full_name}")
