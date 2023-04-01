from marshmallow import Schema, fields


class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)


# De-serializing
json_data = {
    "title": "Test Article",
    "content": "This is a test article",
    "author_id": 1,
}
article_schema = ArticleSchema()
article = article_schema.load(json_data)
print(type(article), article)

# serializing
article_data = article_schema.dump(article)
print(type(article_data), article_data)
