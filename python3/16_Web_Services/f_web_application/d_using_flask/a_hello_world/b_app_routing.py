from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello World!"


# @app.route("/index")
# def hello():
#     return "Hello World!"


@app.route("/")
@app.route("/index")
def hello():
    return "Hello World!"


@app.route("/mypage")
def hello():
    return "Welcome to my Page!"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0", threaded=True, processes=4)
