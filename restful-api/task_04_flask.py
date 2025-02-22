#!/usr/bin/python3
"""
This is the ``task_04_flask`` module
"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {
    "jane": {
        "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"
    },
    "john": {
        "username": "john", "name": "John", "age": 30, "city": "New York"
    },
}


@app.route("/")
def home():
    """Handle root URL"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Handle root URL"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Handle root URL"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Handle root URL"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Handle root URL"""
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    users[data["username"]] = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({
        "message": "User added",
        "user": users[data["username"]]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
