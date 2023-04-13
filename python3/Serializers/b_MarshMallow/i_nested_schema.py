from marshmallow import Schema, fields


class AddressSchema(Schema):
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()


class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    address = fields.Nested(AddressSchema)


class OrganizationSchema(Schema):
    name = fields.Str()
    employees = fields.Nested(PersonSchema, many=True)


address_data = {"street": "123 Main St.", "city": "Anytown", "state": "CA"}

person_data = {"name": "John Doe", "age": 30, "address": address_data}

organization_data = {"name": "Acme Corporation", "employees": [person_data]}

# Serialize data
serialized_data = OrganizationSchema().dumps(organization_data)
print(serialized_data)

# Deserialize data
loaded_data = OrganizationSchema().loads(serialized_data)
print(loaded_data)
