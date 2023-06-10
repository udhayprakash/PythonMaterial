import graphene


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class PersonInput(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()


class Mutation(graphene.ObjectType):
    create_person = graphene.Field(Person, input=PersonInput())

    def resolve_create_person(self, info, input):
        return Person(name=input.name, age=input.age)


schema = graphene.Schema(mutation=Mutation)

mutation = """
    mutation {
        createPerson(input: { name: "John Doe", age: 30 }) {
            name
            age
        }
    }
"""

result = schema.execute(mutation)
print(result.data["createPerson"])
