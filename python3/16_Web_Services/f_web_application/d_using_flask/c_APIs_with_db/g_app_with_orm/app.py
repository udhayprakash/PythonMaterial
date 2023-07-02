from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Book {self.title}>"


# Define the Book schema
class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)
    description = fields.String()


book_schema = BookSchema()
books_schema = BookSchema(many=True)


# Create a new book
@app.route("/books", methods=["POST"])
def create_book():
    new_book = Book(
        title=request.json["title"],
        author=request.json["author"],
        description=request.json["description"],
    )
    db.session.add(new_book)
    db.session.commit()
    return book_schema.dump(new_book), 201


# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify(books_schema.dump(books))


# Get a single book by ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return book_schema.dump(book)


# Update a book by ID
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    book.title = request.json.get("title", book.title)
    book.author = request.json.get("author", book.author)
    book.description = request.json.get("description", book.description)
    db.session.commit()
    return book_schema.dump(book)


# Delete a book by ID
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return "", 204


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # from waitress import serve
    # try:
    #     serve(app, host='0.0.0.0', port=8080)
    # except Exception as e:
    #     print(e)

# gunicorn wsgi:app -c gunicorn.conf.py

# pip install waitress
