import graphene
import sqlalchemy

# Create a database connection
engine = sqlalchemy.create_engine("sqlite:///mydb.sqlite3")


# Create a model
class User(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(50))
    age = sqlalchemy.Column(sqlalchemy.Integer)


# Create a session
session = sqlalchemy.orm.Session(engine)


# Create a GraphQL schema
class Query(graphene.ObjectType):
    users = graphene.List(User)


class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()


schema = graphene.Schema(query=Query)

# Query the database
query = """
query {
  users {
    id
    name
    age
  }
}
"""

result = schema.execute(query)

# Print the results
print(result.data["users"])
