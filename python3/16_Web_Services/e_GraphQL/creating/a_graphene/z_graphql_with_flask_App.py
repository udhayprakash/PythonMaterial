import graphene
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Register the GraphQL schema
schema = graphene.Schema(query=Query)


# Create a GraphQL endpoint
@app.route("/graphql")
def graphql():
    return graphql.graphql(schema, request.args.get("query"))


# Run the app
app.run()
