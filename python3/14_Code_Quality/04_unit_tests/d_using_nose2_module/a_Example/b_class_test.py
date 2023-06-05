class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, my name is {self.name}"


def test_person():
    person = Person("Alice")
    assert person.say_hello() == "Hello, my name is Alice"
