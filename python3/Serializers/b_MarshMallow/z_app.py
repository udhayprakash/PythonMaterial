from flask import Flask
from flask_restplus import Api, Resource, fields
from marshmallow import Schema, ValidationError, fields, post_load
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

# Set up the database engine and session
engine = create_engine("sqlite:///articles.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Define the models for use with SQLAlchemy and Marshmallow
class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<Author {self.name}>"


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", backref=backref("articles", lazy=True))

    def __repr__(self):
        return f"<Article {self.title}>"


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    articles = fields.Nested("ArticleSchema", many=True, exclude=("author",))


class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)
    author = fields.Nested(AuthorSchema, only=("id", "name"))

    @staticmethod
    def _validate_author_id(author_id):
        author = session.query(Author).filter_by(id=author_id).first()
        if not author:
            raise ValidationError(f"Author with ID {author_id} not found.")

    @staticmethod
    def _validate_author(author):
        if not author:
            raise ValidationError("Author not specified.")
        author_id = author.get("id")
        if not author_id:
            raise ValidationError("Author ID not specified.")
        ArticleSchema._validate_author_id(author_id)

    @staticmethod
    def _validate_data(data):
        ArticleSchema._validate_author(data.get("author"))

    @post_load
    def make_article(self, data, **kwargs):
        ArticleSchema._validate_data(data)
        return Article(**data)


# Set up the Flask app and RESTPlus API
app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Article API",
    description="A simple CRUD API for articles, authors, and comments",
)

# Define the models for use in the RESTPlus API
author_model = api.model(
    "Author",
    {"name": fields.String(required=True), "email": fields.String(required=True)},
)

article_model = api.model(
    "Article",
    {
        "title": fields.String(required=True),
        "content": fields.String(required=True),
        "author": fields.Nested(author_model, required=True),
    },
)


# Define the RESTPlus API routes
@api.route("/authors")
class AuthorList(Resource):
    def get(self):
        authors = session.query(Author).all()
        author_schema = AuthorSchema(many=True)
        return author_schema.dump(authors)

    @api.expect(author_model)
    def post(self):
        data = api.payload
        author = Author(**data)
        session.add(author)
        session.commit()
        author_schema = AuthorSchema()
        return author_schema.dump(author)


@api.route("/<int:id>")
class AuthorDetail(Resource):
    @api.response(404, "Author not found")
    def get(self, id):
        author = session.query(Author).filter_by(id=id).first()
        if not author:
            api.abort(404, f"Author with ID {id} not found.")
        author_schema = AuthorSchema()
        return author_schema.dump(author)

    @api.response(404, "Author not found")
    @api.expect(author_model)
    def put(self, id):
        data = api.payload
        author = session.query(Author).filter_by(id=id).first()
        if not author:
            api.abort(404, f"Author with ID {id} not found.")
        author.name = data.get("name")
        author.email = data.get("email")
        session.add(author)
        session.commit()
        author_schema = AuthorSchema()
        return author_schema.dump(author)

    @api.response(404, "Author not found")
    def delete(self, id):
        author = session.query(Author).filter_by(id=id).first()
        if not author:
            api.abort(404, f"Author with ID {id} not found.")
        session.delete(author)
        session.commit()
        return {"message": f"Author with ID {id} deleted successfully."}


# Define the app factory function
def create_app():
    # Set up the database engine and session
    engine = create_engine("sqlite:///articles.db")
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Define the models and schemas here...

    # Set up the Flask app and RESTPlus API
    app = Flask(__name__)
    api = Api(
        app,
        version="1.0",
        title="Article API",
        description="A simple CRUD API for articles, authors, and comments",
    )

    # Define the models for use in the RESTPlus API here...

    # Define the RESTPlus API routes here...

    return app


# Define the main function to start the app
def main():
    app = create_app()
    app.run(host="localhost", port=5000, debug=False)


# Ensure that the app is started only when this script is executed directly
if __name__ == "__main__":
    main()
