from decimal import Decimal

import graphene


class DecimalScalar(graphene.Scalar):
    @staticmethod
    def serialize(value):
        return str(value)

    @staticmethod
    def parse_value(value):
        return Decimal(value)


class Query(graphene.ObjectType):
    pi = DecimalScalar()

    def resolve_pi(self, info):
        return Decimal("3.14159265359")


schema = graphene.Schema(query=Query)

query = """
    query {
        pi
    }
"""

result = schema.execute(query)
print(result.data["pi"])
