import graphene


class Query(graphene.ObjectType):
    greet = graphene.String(name=graphene.String())

    def resolve_greet(self, info, name):
        return f"Hello, {name}!"


schema = graphene.Schema(query=Query)

query = """
    query {
        greet(name: "World")
    }
"""

result = schema.execute(query)
print(result.data["greet"])
