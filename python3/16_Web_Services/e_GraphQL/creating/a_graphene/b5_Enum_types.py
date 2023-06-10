from pprint import pp

import graphene


class Gender(graphene.Enum):
    MALE = "MALE Person"
    FEMALE = "FEMALE Person"
    OTHER = "OTHER Type Person"


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()
    gender = graphene.Field(Gender)


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

    def resolve_person(self, info):
        return Person(name="Gudo Van", age=30, gender=Gender.MALE)


schema = graphene.Schema(query=Query)

query = """
    query {
        person {
            gender
            age
            name
        }
    }
"""

result = schema.execute(query)
pp(result.data)
