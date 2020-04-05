from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)


if __name__ == "__main__":
    app.run()
