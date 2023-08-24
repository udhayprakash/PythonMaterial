import json

from flask import Flask, Response, make_response

app = Flask()


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/endpoint1")
def json_example():
    data = {"key": "value"}
    return json.dumps(data)


@app.route("/endpoint2")
def json_example():
    data = {"key": "value"}
    json_data = json.dumps(data)
    return Response(json_data, mimetype="application/json")


@app.route("/endpoint3")
def json_example():
    data = {"key": "value"}
    json_data = json.dumps(data)

    response = make_response(json_data)
    response.mimetype = "application/json"
    return response


if __name__ == "__main__":
    app.run()
