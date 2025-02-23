from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Endpoint to get all usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Status endpoint
@app.route("/status")
def status():
    return "OK"

# Endpoint to get user details
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
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
