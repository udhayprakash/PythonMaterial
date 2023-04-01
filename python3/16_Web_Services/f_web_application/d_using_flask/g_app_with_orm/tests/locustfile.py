import csv
import random

from locust import HttpUser, between, task

# pip install locust


class BookUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(0.5, 3.0)


class BookUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(0.5, 3.0)

    @task(1)
    def create_book(self):
        with open("books.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        title, author, description = random.choice(rows)
        self.client.post(
            "/books",
            json={"title": title, "author": author, "description": description},
        )

    @task(2)
    def get_books(self):
        self.client.get("/books")

    @task(3)
    def update_book(self):
        book_id = random.randint(1, 100)
        with open("books.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        title, author, description = random.choice(rows)
        self.client.put(
            f"/books/{book_id}",
            json={"title": title, "author": author, "description": description},
        )

    @task(4)
    def delete_book(self):
        book_id = random.randint(1, 100)
        self.client.delete(f"/books/{book_id}")


# to run - locust -f locustfile.py

# Open your web browser and navigate to http://localhost:8089 to access the Locust web interface.
# Enter the number of users and the hatch rate (i.e. the number of users to spawn per second) and start the test. You can also view live statistics and graphs of the test results in the web interface.
