# pip install flask
from flask import Flask

app = Flask(__name__)


@app.route("/")  # endpoint
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    # app.run()
    app.run(port=8000)
