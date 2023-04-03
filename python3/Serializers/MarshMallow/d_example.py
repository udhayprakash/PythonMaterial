from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Int()


user_data = {"name": "John Doe", "email": "johndoe@example.com", "age": 30}

# Serialize the data using the schema
user_schema = UserSchema()
result = user_schema.dump(user_data)
print(result)


# Deserialize the data using the schema
deserialized_user = user_schema.load(result)
print(deserialized_user)
