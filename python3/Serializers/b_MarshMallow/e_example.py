from pprint import pp

from marshmallow import Schema, fields


class PersonSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Integer(required=True)
    email = fields.Email(required=True)
    is_active = fields.Boolean(default=True)
    interests = fields.List(fields.Str(), required=True)


data = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "interests": ["hiking", "reading", "cooking"],
}

# Load the data into the schema
loaded_data = PersonSchema().load(data)

# Dump the data back out of the schema
dumped_data = PersonSchema().dump(loaded_data)

pp(dumped_data)
