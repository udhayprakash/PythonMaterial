from pprint import pp

import graphene


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()
    height = graphene.Float()
    is_student = graphene.Boolean()
    birth_date = graphene.Date()
    address = graphene.String()
    email = graphene.String()
    phone_numbers = graphene.List(graphene.String)
    favorite_numbers = graphene.List(graphene.Int)
    grades = graphene.List(graphene.Float)
    profile_picture = graphene.Field(graphene.String)
    friends = graphene.List(lambda: Person)


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

    def resolve_person(self, info):
        return Person(
            name="John Doe",
            age=30,
            height=175.5,
            is_student=True,
            birth_date="1990-01-01",
            address="123 Main St",
            email="john.doe@example.com",
            phone_numbers=["123-456-7890", "987-654-3210"],
            favorite_numbers=(42, 7, 13),
            grades={98.5, 85.0, 91.3},
            profile_picture="https://example.com/profile_picture.jpg",
            friends=[
                Person(name="Jane Smith", age=28),
                Person(name="Bob Johnson", age=32),
            ],
        )


schema = graphene.Schema(query=Query)

query = """
    query {
        person {
            name
            age
            height
            isStudent
            birthDate
            address
            email
            phoneNumbers
            favoriteNumbers
            grades
            profilePicture
            friends {
                name
                age
            }
        }
    }
"""

result = schema.execute(query)
pp(result.data)
# print(result.data['person'])
