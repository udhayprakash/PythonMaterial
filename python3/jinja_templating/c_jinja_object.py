from jinja2 import Template


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


person = Person('Peter', 34)

tm = Template("My name is {{ per.get_name() }} and I am {{ per.get_age() }}")
msg = tm.render(per=person)

print(msg)
