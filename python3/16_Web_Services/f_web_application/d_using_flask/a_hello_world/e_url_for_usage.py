from flask import Flask, url_for

app = Flask(__name__)


@app.route("/", endpoint="home")
def index():
    return "Hello, World!"


@app.route("/user/<username>", endpoint="profile")
def user(username):
    return f"Hello, {username}!"


with app.test_request_context():
    print(url_for("home"))  # outputs '/'
    print(url_for("profile", username="john"))  # outputs '/user/john'


if __name__ == "__main__":
    app.run(debug=True)
