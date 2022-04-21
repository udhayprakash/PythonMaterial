from flask import request, Flask, jsonify, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect(url_for("foo"))


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    """To respond Requester IP address"""
    return jsonify({"ip": request.remote_addr}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
