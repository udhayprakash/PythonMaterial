from pprint import pp

import graphene


# Define the User object type
class User(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


# Define the Query object type
class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        # Simulated user data
        user_data = [
            {"name": "John Doe", "age": 30},
            {"name": "Jane Smith", "age": 25},
            {"name": "Bob Johnson", "age": 35},
        ]

        # Convert user data to User objects
        return [User(name=user["name"], age=user["age"]) for user in user_data]


# Create the schema
schema = graphene.Schema(query=Query)


# Execute the query with the fragment
query = """
    fragment User on User {
        name
        age
    }

    query {
        users {
            ...User
        }
    }
"""

result = schema.execute(query)

# Print the query result
if result.errors:
    print(f"Query errors: {result.errors}")
else:
    pp(result.data)
