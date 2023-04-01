from marshmallow import Schema, fields

# class PersonSchema(Schema):
#     name = fields.Str()
#     age = fields.Int()


# Validating
class PersonSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)


def validate_person(person_record):
    schema = PersonSchema()
    try:
        result = schema.load(person_record)
        print(result)
    except Exception as ex:
        print(ex.messages)  # {'age': ['Missing data for required field.']}


validate_person({"name": "John Doe", "age": 30})
validate_person({"name": "John Doe", "age": 30.3})
validate_person({"name": r"John Doe", "age": 30.3})
validate_person({"name": b"John Doe", "age": 30.3})
validate_person({"name": "John Doe", "age": 30.3})
print()

validate_person({"name": "John Doe", "age": True})
validate_person({"name": "John Doe"})
print()
validate_person({"name": 121, "age": 30})
validate_person({"name": 121})
validate_person({})
