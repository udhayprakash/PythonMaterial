from pprint import pp

from marshmallow import Schema, fields


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    comments = fields.Nested(CommentSchema, many=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    posts = fields.Nested(PostSchema, many=True)


user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "posts": [
        {
            "title": "My First Post",
            "content": "Hello World!",
            "comments": [{"text": "Great post!"}, {"text": "Thanks for sharing."}],
        },
        {
            "title": "My Second Post",
            "content": "Goodbye World!",
            "comments": [{"text": "So sad to see you go."}],
        },
    ],
}

# Load the data into the schema
loaded_data = UserSchema().load(user_data)

# Dump the data back out of the schema
dumped_data = UserSchema().dump(loaded_data)

pp(dumped_data)
