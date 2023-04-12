from flask import Flask, request
from flask_restplus import Api, Resource, fields
from models import Article, Author, Comment
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the Flask app and RESTPlus API
app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Article API",
    description="A simple CRUD API for articles, authors, and comments",
)

# # Set up the database engine and session
# engine = create_engine('postgresql://username:password@localhost/db_name')

# SQLAlchemy configuration
engine = create_engine("sqlite:///articles.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

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
        "author_id": fields.Integer(required=True),
    },
)

comment_model = api.model(
    "Comment",
    {
        "content": fields.String(required=True),
        "author_id": fields.Integer(required=True),
        "article_id": fields.Integer(required=True),
    },
)


# Define the RESTPlus API routes
@api.route("/authors")
class AuthorList(Resource):
    def get(self):
        authors = session.query(Author).all()
        return [author.__dict__ for author in authors]

    @api.expect(author_model)
    def post(self):
        data = api.payload
        author = Author(**data)
        session.add(author)
        session.commit()
        return author.__dict__


@api.route("/authors/<int:id>")
class AuthorDetail(Resource):
    def get(self, id):
        author = session.query(Author).filter(Author.id == id).first()
        if author:
            return author.__dict__
        else:
            api.abort(404, f"Author {id} not found.")

    @api.expect(author_model)
    def put(self, id):
        author = session.query(Author).filter(Author.id == id).first()
        if author:
            data = api.payload
            author.name = data.get("name", author.name)
            author.email = data.get("email", author.email)
            session.commit()
            return author.__dict__
        else:
            api.abort(404, f"Author {id} not found.")

    def delete(self, id):
        author = session.query(Author).filter(Author.id == id).first()
        if author:
            session.delete(author)
            session.commit()
            return {"message": f"Author {id} deleted."}
        else:
            api.abort(404, f"Author {id} not found.")


@api.route("/articles")
class ArticleList(Resource):
    def get(self):
        articles = session.query(Article).all()
        return [article.__dict__ for article in articles]

    @api.expect(article_model)
    def post(self):
        data = api.payload
        article = Article(**data)
        session.add(article)
        session.commit()
        return article.__dict__


@api.route("/articles/<int:id>")
class ArticleDetail(Resource):
    def get(self, id):
        article = session.query(Article).filter(Article.id == id).first()
        if article:
            return article.__dict__
        else:
            api.abort(404, f"Article {id} not found.")

    @api.expect(article_model)
    def put(self, id):
        article = session.query
