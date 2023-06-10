"""
GraphQL subscriptions provide a way to receive real-time updates from a server

"""

import graphene
import graphql


class User(graphene.ObjectType):
    """A user."""

    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()


class Query(graphene.ObjectType):
    """The root query type."""

    # This is the query that will be used to subscribe to new users.
    new_user = graphene.Field(User)


class Subscription(graphene.ObjectType):
    new_user = graphene.Field(User)


schema = graphene.Schema(query=Query, subscription=Subscription)

# Create a subscription
subscription = schema.subscribe("new_user")

# Listen for new users
while True:
    data = subscription.next()
    if data is not None:
        print(data)
