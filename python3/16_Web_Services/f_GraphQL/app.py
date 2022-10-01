import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "World") -> str:
        return f"Hello {name}"


schema = strawberry.Schema(query=Query)
