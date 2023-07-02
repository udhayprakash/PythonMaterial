from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}!"


with app.test_request_context():
    print(url_for("index"))  # outputs '/'
    print(url_for("user", username="john"))  # outputs '/user/john'


if __name__ == "__main__":
    app.run(debug=True)
