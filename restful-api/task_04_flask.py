#!/usr/bin/python3
"""
This is the ``task_04_flask`` module
"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return a list of usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return a status message."""
    return jsonify({"status": "OK"})


@app.route("/users/<username>")
def get_user(username):
    """Return user details by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
