"""
Purpose: REST API with all CRUD operations

    GET /todos - Retrieve all todos
    POST /todos - Create a new todo
    PUT /todos/{id} - Update a specific todo by ID
    DELETE /todos/{id} - Delete a specific todo by ID

"""
import json
from http.server import BaseHTTPRequestHandler

todos = [
    {"id": 1, "task": "Finish homework", "completed": False},
    {"id": 2, "task": "Buy groceries", "completed": True},
]


class TodoHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def _parse_request_data(self):
        content_length = int(self.headers["Content-Length"])
        request_data = self.rfile.read(content_length).decode("utf-8")
        return json.loads(request_data)

    def do_GET(self):
        if self.path == "/todos":
            self._set_response()
            self.wfile.write(json.dumps(todos).encode())

    def do_POST(self):
        if self.path == "/todos":
            data = self._parse_request_data()
            new_todo = {
                "id": len(todos) + 1,
                "task": data.get("task"),
                "completed": False,
            }
            todos.append(new_todo)
            self._set_response(201)
            self.wfile.write(json.dumps(new_todo).encode())

    def do_PUT(self):
        if self.path.startswith("/todos/"):
            todo_id = int(self.path.split("/")[-1])
            data = self._parse_request_data()
            for todo in todos:
                if todo["id"] == todo_id:
                    todo["task"] = data.get("task")
                    todo["completed"] = data.get("completed")
                    self._set_response()
                    self.wfile.write(json.dumps(todo).encode())
                    return
            self._set_response(404)
            self.wfile.write(b"Todo not found")

    def do_DELETE(self):
        if self.path.startswith("/todos/"):
            todo_id = int(self.path.split("/")[-1])
            for todo in todos:
                if todo["id"] == todo_id:
                    todos.remove(todo)
                    self._set_response(204)
                    return
            self._set_response(404)
            self.wfile.write(b"Todo not found")


if __name__ == "__main__":
    from http.server import HTTPServer

    server = HTTPServer(("localhost", 8000), TodoHandler)
    print("Server running on localhost:8000...")
    server.serve_forever()
