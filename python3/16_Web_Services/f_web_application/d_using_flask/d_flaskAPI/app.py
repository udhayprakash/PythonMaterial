from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for testing
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
    },
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]


# Create
@app.route("/books", methods=["POST"])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "year": request.json["year"],
    }
    books.append(new_book)
    return jsonify(new_book)


# Read all
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


# Read one
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    if len(book) == 0:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book[0])


# Update
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    if len(book) == 0:
        return jsonify({"error": "Book not found"}), 404
    book[0]["title"] = request.json.get("title", book[0]["title"])
    book[0]["author"] = request.json.get("author", book[0]["author"])
    book[0]["year"] = request.json.get("year", book[0]["year"])
    return jsonify(book[0])


# Delete
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    if len(book) == 0:
        return jsonify({"error": "Book not found"}), 404
    books.remove(book[0])
    return jsonify({"result": True})
