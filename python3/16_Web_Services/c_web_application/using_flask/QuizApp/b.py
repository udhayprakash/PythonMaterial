from flask import Flask

app = Flask(__name__)


@app.route('/')
def quiz():
    return '<h1>Quiz Here</h1>'


if __name__ == '__main__':
    app.run(debug=True)
