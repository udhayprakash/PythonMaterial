import ast
from datetime import datetime
from pprint import pp

import graphene


class DateTime(graphene.Scalar):
    @staticmethod
    def serialize(dt):
        return dt.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.fromisoformat(node.value)

    @staticmethod
    def parse_value(value):
        return datetime.fromisoformat(value)


class Query(graphene.ObjectType):
    current_time = graphene.Field(DateTime)

    def resolve_current_time(self, info):
        return datetime.now()


schema = graphene.Schema(query=Query)

query = """
    query {
        currentTime
    }
"""

result = schema.execute(query)
pp(result.data)
print()

print(result.data["currentTime"])  # 2023-06-09T16:38:25.911552
