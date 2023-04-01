from pprint import pp

from marshmallow import Schema, fields, validate


class PersonSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    email = fields.Email()
    age = fields.Integer(validate=validate.Range(min=0, max=150))
    is_active = fields.Boolean()
    score = fields.Float()
    created_at = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    data = fields.Dict()
    tags = fields.List(fields.String())


data = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "is_active": True,
    "score": 8.5,
    "created_at": "2022-03-31 15:30:00",
    "data": {"foo": "bar", "baz": 123},
    "tags": ["tag1", "tag2", "tag3"],
}

# Load the data into the schema
loaded_data = PersonSchema().load(data)

# Dump the data back out of the schema
dumped_data = PersonSchema().dump(loaded_data)

pp(dumped_data)
