from flask import Flask, request, jsonify

app = Flask(__name__)
users = []

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User registered!", "user": data}), 201

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
