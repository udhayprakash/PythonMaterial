import sentry_sdk
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration

# Configure Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/b_test.db"

# Configure Sentry
sentry_sdk.init(
    dsn="https://4990dbc96cc34e72a1e0045ae45141bf@o386823.ingest.sentry.io/4505460829257728",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)

# Initialize the database
db = SQLAlchemy(app)


# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }


# Create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    try:
        data = request.json
        title = data.get("title")
        description = data.get("description")
        status = data.get("status")

        if not title or not description or not status:
            return jsonify({"error": "Missing required fields"}), 400

        task = Task(title=title, description=description, status=status)
        db.session.add(task)
        db.session.commit()

        return (
            jsonify({"message": "Task created successfully", "task": task.to_dict()}),
            201,
        )

    except Exception as e:
        sentry_sdk.capture_exception(e)
        return jsonify({"error": "An error occurred while creating the task"}), 500


# Get task details
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        task = Task.query.get(task_id)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        return jsonify({"task": task.to_dict()})

    except Exception as e:
        sentry_sdk.capture_exception(e)
        return jsonify({"error": "An error occurred while fetching the task"}), 500


# Update task details
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        task = Task.query.get(task_id)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        data = request.json
        title = data.get("title")
        description = data.get("description")
        status = data.get("status")

        if not title or not description or not status:
            return jsonify({"error": "Missing required fields"}), 400

        task.title = title
        task.description = description
        task.status = status

        db.session.commit()

        return jsonify({"message": "Task updated successfully", "task": task.to_dict()})

    except Exception as e:
        sentry_sdk.capture_exception(e)
        return jsonify({"error": "An error occurred while updating the task"}), 500


# Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted successfully"})

    except Exception as e:
        sentry_sdk.capture_exception(e)
        return jsonify({"error": "An error occurred while deleting the task"}), 500


if __name__ == "__main__":
    app.run(debug=True)
