from pprint import pp

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello, GraphQL!"


schema = graphene.Schema(query=Query)
print(f"{schema =}")

query = """
    query {
        hello
    }
"""

result = schema.execute(query)
pp(result.data)

print(result.data["hello"])
