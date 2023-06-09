from pprint import pp

import graphene


class Animal(graphene.Interface):
    name = graphene.String()


class Dog(graphene.ObjectType):
    class Meta:
        interfaces = (Animal,)

    breed = graphene.String()


class Cat(graphene.ObjectType):
    class Meta:
        interfaces = (Animal,)

    color = graphene.String()


class Query(graphene.ObjectType):
    animal = graphene.Field(Animal)

    def resolve_animal(self, info):
        return Dog(name="Buddy", breed="Labrador Retriever")


schema = graphene.Schema(query=Query)

query = """
    query {
        animal {
            name
            ... on Dog {
                breed
            }
            ... on Cat {
                color
            }
        }
    }
"""

result = schema.execute(query)
pp(result.data)
