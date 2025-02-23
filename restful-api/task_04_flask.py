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


@app.route('/')
def home():
    """Handle root URL"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Display data"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Display Status"""
    return "OK"


@app.route('/users/<username>')
def userInfo(username):
    """Display specified user"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
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
