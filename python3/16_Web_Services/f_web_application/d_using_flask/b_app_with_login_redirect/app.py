# importing redirect
from flask import Flask, abort, redirect, render_template, request, url_for

# Initialize the flask application
app = Flask(__name__)


@app.route("/")
def index():
    """It will load the form template which is in login.html"""
    return render_template("login.html")


@app.route("/success")
def success():
    return "logged in successfully"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST" and request.form["username"] == "admin":
        return redirect(url_for("success"))

    return redirect(url_for("index"))


@app.route("/<uname>")
def index(uname):
    if uname[0].isdigit():
        abort(403)
    return "<h1>Good Username</h1>"


if __name__ == "__main__":
    app.run(debug=True)
