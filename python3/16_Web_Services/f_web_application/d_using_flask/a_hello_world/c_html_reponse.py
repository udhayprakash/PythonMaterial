from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/detail")
def detail():
    return """
        <h1> Hello world </h1>
        <h2> Hello world </h2>
        <h3> Hello world </h3>
        <h4> Hello world </h4>
        <h5> Hello world </h5>

        <p> Hello world</p>
    """


# @app.route("/user/")
# def user(name):
#     return "<h1>Specify the User" % name


# @app.route("/user/name")
@app.route("/user/<name>")
def user(name):
    return f"<h1>Name is {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
