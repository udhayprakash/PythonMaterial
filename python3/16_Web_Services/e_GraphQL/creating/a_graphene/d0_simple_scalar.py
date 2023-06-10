import graphene


# Define a custom scalar type
class CustomScalar(graphene.Scalar):
    @staticmethod
    def serialize(value):
        # return value
        return str(value).upper()

    @staticmethod
    def parse_literal(node):
        return node.value

    @staticmethod
    def parse_value(value):
        return value


# Define a query object
class Query(graphene.ObjectType):
    custom_value = graphene.Field(CustomScalar)

    def resolve_custom_value(self, info):
        return "Hello, World!"


# Create a schema and execute a query
schema = graphene.Schema(query=Query)

query = """
    query {
        customValue
    }
"""

result = schema.execute(query)
print(result.data)  # {'customValue': 'Hello, World!'}
