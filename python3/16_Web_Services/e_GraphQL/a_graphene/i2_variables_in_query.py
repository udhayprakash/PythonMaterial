from pprint import pp

import graphene


class Query(graphene.ObjectType):
    greet = graphene.String(name=graphene.String())

    def resolve_greet(self, info, name):
        return f"Hello, {name}!"


schema = graphene.Schema(query=Query)

query = """
    query ($name: String!) {
        greet(name: $name)
    }
"""

variables = {"name": "Gudo"}

result = schema.execute(query, variable_values=variables)
pp(result.data)
print(result.data["greet"])
