#!/usr/bin/python
"""
Purpose: Creating a REST API using bottle framework
"""

from bottle import run, get, post, delete

persons = [
    {"name": "Udhay", "age": 30, "city": "Hyderabad"},
    {"name": "Prakash", "age": 56, "city": "New Delhi"},
    {"name": "someone", "age": 99, "city": "Mumbai"},
]


@get("/persons")
def get_all():
    return {"persons": persons}


@get("/persons/<name>")
def get_one(name):
    person_details = [person for person in persons if person["name"] == name]
    return {"person_details": person_details}


@post("/persons/")
def add_one(request):
    new_person = {
        "name": request.json.get("name"),
        "age": request.json.get("age"),
        "city": request.json.get("city"),
    }
    persons.append(new_person)
    return {"persons": persons}


@delete("/persons/<name>")
def remove_one(name):
    removing_person = [person for person in persons if person["name"] == name]
    persons.remove(removing_person)
    return {"persons": persons}


# To start the server
run(reloader=True, debug=True)
