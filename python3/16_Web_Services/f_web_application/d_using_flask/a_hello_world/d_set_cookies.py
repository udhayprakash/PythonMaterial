from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def index():
    # return '<h1>Hello World!</h1>'
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie("answer", "42")
    return response


@app.route("/user/")
def user(name):
    return "<h1>Specify the User" % name


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, %s!</h1>" % name


if __name__ == "__main__":
    app.run(debug=True)
