from datetime import datetime

import graphene


class DateTime(graphene.DateTime):
    @staticmethod
    def serialize(dt):
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def parse_value(value):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


class Query(graphene.ObjectType):
    current_time = DateTime()

    def resolve_current_time(self, info):
        return datetime.now()


schema = graphene.Schema(query=Query)

query = """
    query {
        currentTime
    }
"""

result = schema.execute(query)
print(result.data["currentTime"])
