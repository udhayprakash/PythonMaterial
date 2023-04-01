from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)
    article_id = fields.Int(required=True)


class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)
    comments = fields.Nested(CommentSchema, many=True)


# Example usage for serializing and deserializing an Article object
author_data = {"name": "John Smith", "email": "john.smith@example.com"}
author_schema = AuthorSchema()
author = author_schema.load(author_data)

comment_data = [
    {"content": "Great article!", "author_id": 1, "article_id": 1},
    {"content": "Thanks for writing this.", "author_id": 2, "article_id": 1},
]
comment_schema = CommentSchema(many=True)
comments = comment_schema.load(comment_data)

article_data = {
    "title": "Test Article",
    "content": "This is a test article",
    "author_id": 1,
    "comments": comments,
}
article_schema = ArticleSchema()
article = article_schema.load(article_data)

print(article)
