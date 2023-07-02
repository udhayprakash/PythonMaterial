import unittest

from app import Book, app, db


class TestBookAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        db.session.add(
            Book(title="Book 1", author="Author 1", description="Description 1")
        )
        db.session.add(
            Book(title="Book 2", author="Author 2", description="Description 2")
        )
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_book(self):
        response = self.client.post(
            "/books",
            json={
                "title": "Book 3",
                "author": "Author 3",
                "description": "Description 3",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["title"], "Book 3")
        self.assertEqual(response.json["author"], "Author 3")
        self.assertEqual(response.json["description"], "Description 3")

    def test_get_books(self):
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

    def test_get_book(self):
        book_id = Book.query.filter_by(title="Book 1").first().id
        response = self.client.get(f"/books/{book_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["title"], "Book 1")
        self.assertEqual(response.json["author"], "Author 1")
        self.assertEqual(response.json["description"], "Description 1")

    def test_update_book(self):
        book_id = Book.query.filter_by(title="Book 1").first().id
        response = self.client.put(
            f"/books/{book_id}", json={"title": "Updated Book 1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["title"], "Updated Book 1")
        self.assertEqual(response.json["author"], "Author 1")
        self.assertEqual(response.json["description"], "Description 1")

    def test_delete_book(self):
        book_id = Book.query.filter_by(title="Book 1").first().id
        response = self.client.delete(f"/books/{book_id}")
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Book.query.get(book_id))
