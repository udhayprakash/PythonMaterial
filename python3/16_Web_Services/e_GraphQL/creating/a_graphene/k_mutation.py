"""
Purpose: Mutations

    mutation is a way to modify data on the server
        - Modifying data - CRUD operations
        - Explicitly Defined

"""

from graphene import Mutation, ObjectType, Schema, String

# Step 1: Define the mutation


class CreateUserMutation(Mutation):
    class Arguments:
        username = String(required=True)
        password = String(required=True)

    success_message = String()

    def mutate(self, info, username, password):
        # Perform your mutation logic here
        # For simplicity, let's just print the input values
        print(f"Creating user: {username}, password: {password}")
        self.success_message = f"User {username} created successfully"
        return self


# Step 2: Define the mutation's output type


class CreateUserMutationOutput(ObjectType):
    success_message = String()


# Step 3: Define the root mutation object


class MutationRoot(ObjectType):
    create_user = CreateUserMutation.Field()


# Step 4: Define the query schema

schema = Schema(mutation=MutationRoot)


# Step 5: Execute the mutation

if __name__ == "__main__":
    mutation_input = {"username": "john_doe", "password": "password123"}

    result = schema.execute(
        """
        mutation createUser($input: CreateUserMutationInput!) {
            createUser(input: $input) {
                successMessage
            }
        }
    """,
        variable_values={"input": mutation_input},
    )

    # Step 6: Handle the mutation result

    if result.errors:
        print(f"Mutation errors: {result.errors}")
    else:
        print(f"Mutation result: {result.data}")
