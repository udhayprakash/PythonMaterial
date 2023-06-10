from pprint import pprint

import graphene


class Gender(graphene.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

    @property
    def description(self):
        if self == Gender.MALE:
            return "Male gender"
        elif self == Gender.FEMALE:
            return "Female gender"
        elif self == Gender.OTHER:
            return "Other gender"


class Person(graphene.ObjectType):
    name = graphene.String(description="The name of the person.")
    age = graphene.Int(description="The age of the person.")
    gender = graphene.Field(
        Gender,
        description="The gender of the person. Possible values: MALE, FEMALE, OTHER.",
    )


class Query(graphene.ObjectType):
    person = graphene.Field(Person, description="Get information about a person.")

    def resolve_person(self, info):
        return Person(name="John Doe", age=30, gender=Gender.MALE)


schema = graphene.Schema(query=Query)

query = """
    query {
        person {
            name
            age
            gender
        }
    }
"""

result = schema.execute(query)
pprint(result.data)
