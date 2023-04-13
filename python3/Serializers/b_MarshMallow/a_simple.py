from marshmallow import Schema, fields


class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()


# Deserializing JSON to Python objects
data = {"name": "John Doe", "age": 30}
schema = PersonSchema()
result = schema.load(data)
print(result)  # {'name': 'John Doe', 'age': 30}


# Serializing Python objects to JSON
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John Doe", 30)
schema = PersonSchema()
result = schema.dump(person)
print(result)  # {'name': 'John Doe', 'age': 30}
