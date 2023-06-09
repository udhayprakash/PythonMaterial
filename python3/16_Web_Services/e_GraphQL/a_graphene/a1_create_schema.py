from pprint import pp

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello, GraphQL!"


schema = graphene.Schema(query=Query)
print(f"{schema =}")

pp(vars(schema))
"""
{'query': <Query meta=<ObjectTypeOptions name='Query'>>,
 'mutation': None,
 'subscription': None,
 'graphql_schema': <graphql.type.schema.GraphQLSchema object at 0x000002B1366B0390>}
"""

print(dir(schema))
# ['execute', 'execute_async', 'graphql_schema', 'introspect', 'lazy', 'mutation', 'query', 'subscribe', 'subscription']
