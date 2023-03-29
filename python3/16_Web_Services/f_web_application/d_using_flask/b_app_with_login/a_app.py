from flask import Flask, render_template

# app = Flask(__name__)
app = Flask("myapp")


@app.route("/")
def index():
    return render_template("index.html")
    return "<h1>Hello, World!</h1>"
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
