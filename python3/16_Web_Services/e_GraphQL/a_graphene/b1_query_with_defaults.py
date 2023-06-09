from pprint import pp

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    # def resolve_hello(self, info):
    #     return 'Hello, GraphQL!'

    def resolve_hello(self, info, name):
        # print(f"{info =}\n")
        return "Hello " + name


schema = graphene.Schema(query=Query)
print(f"{schema =}")

# query = '''
#     query {
#         hello
#     }
# '''

query = "{ hello }"

result = schema.execute(query)
pp(result.data)

print(result.data["hello"])
