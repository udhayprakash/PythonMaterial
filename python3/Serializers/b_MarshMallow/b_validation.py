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
        print(ex.messages)


validate_person({"name": "John Doe", "age": 30})
validate_person({"name": "John Doe", "age": 30.3})
validate_person({"name": r"John Doe", "age": 30.3})
validate_person({"name": b"John Doe", "age": 30.3})
validate_person({"name": "John Doe", "age": 30.3})
print()

validate_person({"name": "John Doe", "age": True})  # {'age': ['Not a valid integer.']}
validate_person({"name": "John Doe"})  # {'age': ['Missing data for required field.']}
print()

validate_person({"name": 121, "age": 30})  # {'name': ['Not a valid string.']}
validate_person({"name": 121})
# {'name': ['Not a valid string.'], 'age': ['Missing data for required field.']}

print()

validate_person({})
# {'name': ['Missing data for required field.'], 'age': ['Missing data for required field.']}
