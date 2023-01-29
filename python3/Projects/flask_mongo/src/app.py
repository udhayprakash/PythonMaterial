#!/usr/bin/python3
"""
Purpose: Simple REST API with two end points
"""
from bson.json_util import dumps as bson_dumps
from bson.objectid import ObjectId
from flask import Flask
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

app = Flask(__name__)

# allows REST service from other langauges
CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.flask_mongoDB
if "users" in db.list_collection_names():
    users_collection = db.get_collection("users")
else:
    users_collection = db.create_collection("users")


@app.route("/")
@cross_origin()
def get_all_users():
    """Endpoint to get all users"""
    result = list(users_collection.find({}))
    return bson_dumps(result)


@app.route("/users/<user_id>")
@cross_origin()
def get_user_details(user_id="5f481bcafcedab42c8652d73"):
    """Endpoint to get user details, for specific given users"""
    result = list(users_collection.find({"_id": ObjectId(user_id)}))
    return bson_dumps(result)


if __name__ == "__main__":
    app.run()
