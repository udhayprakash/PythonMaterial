from pprint import pp

import graphene


class Person(graphene.ObjectType):
    name = graphene.String(description="The name of the person.")
    age = graphene.Int(description="The age of the person.")


class Query(graphene.ObjectType):
    person = graphene.Field(Person, description="Get information about a person.")

    def resolve_person(self, info):
        return Person(name="John Doe", age=30)


schema = graphene.Schema(query=Query)

# Execute a query to introspect the schema
introspection_query = """
    query IntrospectionQuery {
        __schema {
            types {
                name
                kind
                description
                fields {
                    name
                    description
                }
            }
        }
    }
"""

result = schema.execute(introspection_query)
pp(result.data)
