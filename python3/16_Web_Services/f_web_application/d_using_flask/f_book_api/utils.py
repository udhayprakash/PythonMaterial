import json


def get_books():
    with open("books.json", "r") as fh:
        books = json.load(fh)
    return books
