from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker

# Set up the database engine
engine = create_engine("postgresql://username:password@localhost/db_name")

# Define the declarative base
Base = declarative_base()


# Define the Author model
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    articles = relationship("Article", backref="author")


# Define the Article model
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))


# Define the Comment model
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))


# Define the get_comment_count function
def get_comment_count(article_id):
    session = Session()
    comment_count = (
        session.query(func.count(Comment.id))
        .filter(Comment.article_id == article_id)
        .scalar()
    )
    session.close()
    return comment_count


# Create the tables
Base.metadata.create_all(engine)

# Set up a session to interact with the database
Session = sessionmaker(bind=engine)
