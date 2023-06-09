from pprint import pp

import graphene


class Dog(graphene.ObjectType):
    name = graphene.String()
    breed = graphene.String()


class Cat(graphene.ObjectType):
    name = graphene.String()
    color = graphene.String()


class Pet(graphene.Union):
    class Meta:
        types = (Dog, Cat)


class Query(graphene.ObjectType):
    pet = graphene.Field(Pet)

    def resolve_pet(self, info):
        return Dog(name="Buddy", breed="Labrador Retriever")


schema = graphene.Schema(query=Query)

query = """
    query {
        pet {
            __typename
            ... on Dog {
                name
                breed
            }
            ... on Cat {
                name
                color
            }
        }
    }
"""

result = schema.execute(query)
pp(result.data)
