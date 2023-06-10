from pprint import pp

import graphene


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

    def resolve_person(self, info):
        return Person(name="Gudo Van", age=67)


schema = graphene.Schema(query=Query)

query = """
    query {
        person {
            name
            age
        }
    }
"""

result = schema.execute(query)
print(f"{result.data       = }")  # {'person': {'name': 'Gudo Van', 'age': 67}}
print(f"{result.formatted  = }")
print()

print(f"{result.errors     = }")
print(f"{result.extensions = }")
print()


query = """
    query {
        person {
            name
        }
    }
"""

result = schema.execute(query)
print(f"{result.data       = }")  # {'person': {'name': 'Gudo Van'}}
print(f"{result.formatted  = }")
