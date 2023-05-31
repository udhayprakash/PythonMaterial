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

    @property
    def full_name(self):
        return self.first + " " + self.last

    @property
    def full_name_in_upper_case(self):
        # return (self.first + " " + self.last).upper()
        return self.full_name.upper()


person1 = Person("Udhay", "Prakash")

print(f"person1.first      :{person1.first}")
print(f"person1.last       :{person1.last}")

print(person1.email())
print()

# person1.full_name()
# TypeError: 'str' object is not callable

# After placing property decorator, method
# should be accessed like a variable

print(f"{person1.full_name =}")
print(f"{person1.full_name_in_upper_case =}")
