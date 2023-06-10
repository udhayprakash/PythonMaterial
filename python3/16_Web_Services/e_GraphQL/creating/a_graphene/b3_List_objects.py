from pprint import pp

import graphene


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class Query(graphene.ObjectType):
    people = graphene.List(Person)

    def resolve_people(self, info):
        return [Person(name="Udhay Prakash", age=30), Person(name="Prem Smith", age=66)]


schema = graphene.Schema(query=Query)

query = """
    query {
        people {
            age
            name
        }
    }
"""
result = schema.execute(query)
pp(result.data)

"""
{'people': [{'age': 30, 'name': 'Udhay Prakash'},
            {'age': 66, 'name': 'Prem Smith'}]}
"""
