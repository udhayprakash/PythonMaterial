from flask import Flask, jsonify, request

app = Flask(__name__)

# http methods - GET , post , put , delete

# CRUD operations
# Create - POST
# Read  - GET
# Update - PUT/PATCH
# Delete   - DELETE

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
    },
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]


@app.route("/books", methods=["POST"])
def create():
    new_book = {
        "id": books[-1]["id"] + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "year": request.json["year"],
    }
    books.append(new_book)
    return jsonify(new_book), 201  # 201 - created


# GEt all
@app.route("/books", methods=["GET"])
def all_books():
    return jsonify(books)


# Get specific one
@app.route("/books/<int:book_id>", methods=["GET"])
def get_specific_book(book_id):
    specific_book = [book for book in books if book["id"] == book_id]
    if len(specific_book) == 0:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(specific_book[0])


# update
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    specific_book = [book for book in books if book["id"] == book_id]
    if len(specific_book) == 0:
        return jsonify({"error": "Book not found"}), 404

    specific_book[0]["title"] = request.json["title"]
    specific_book[0]["author"] = request.json["author"]
    specific_book[0]["year"] = request.json["year"]
    return jsonify(specific_book[0])


# Delete
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    specific_book = [book for book in books if book["id"] == book_id]
    if len(specific_book) == 0:
        return jsonify({"error": "Book not found"}), 404

    books.remove(specific_book[0])
    return jsonify({"message": "Book successfully deleted"})


if __name__ == "__main__":
    app.run(debug=True)
