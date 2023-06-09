from pprint import pp

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello, GraphQL!"


schema = graphene.Schema(query=Query)


query = """
    query {
        __schema {
            types {
                name
                kind
            }
        }
    }
"""

result = schema.execute(query)
pp(result.data)
print()

print(result.data["__schema"]["types"])
