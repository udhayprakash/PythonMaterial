import json

from flask import Flask, jsonify, request
from utils import get_books

app = Flask(__name__)


@app.route("/books", methods=["POST"])
def create():
    new_book = {
        "id": books[-1]["id"] + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "year": request.json["year"],
    }
    books = get_books()
    books.append(new_book)
    with open("books.json", "a") as fh:
        json.dump(books, fh)

    return jsonify(new_book), 201  # 201 - created


# GEt all
@app.route("/books", methods=["GET"])
def all_books():
    books = get_books()
    return jsonify(books)


# Get specific one
@app.route("/books/<int:book_id>", methods=["GET"])
def get_specific_book(book_id):
    books = get_books()
    specific_book = [book for book in books if book["id"] == book_id]
    if len(specific_book) == 0:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(specific_book[0])


# update
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    books = get_books()
    book_index = None
    for index, book in enumerate(books):
        if book["id"] == book_id:
            book_index = index

    if book_index is None:
        return jsonify({"error": "Book not found"}), 404

    books[book_index]["title"] = request.json["title"]
    books[book_index]["author"] = request.json["author"]
    books[book_index]["year"] = request.json["year"]

    with open("books.json", "w") as fh:
        json.dump(books, fh)
    return jsonify(books[book_index])


# Delete
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    books = get_books()
    book_index = None
    for index, book in enumerate(books):
        if book["id"] == book_id:
            book_index = index

    if book_index is None:
        return jsonify({"error": "Book not found"}), 404

    del books[book_index]
    return jsonify({"message": "Book successfully deleted"})


if __name__ == "__main__":
    app.run(debug=True)
