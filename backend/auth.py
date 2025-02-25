from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from config import SECRET_KEY
from database import users_collection

auth_bp = Blueprint("auth", __name__)

def create_token(user_id):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email, password = data.get("email"), data.get("password")

    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"email": email, "password": hashed_password})
    return jsonify({"message": "User registered successfully!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email, password = data.get("email"), data.get("password")

    user = users_collection.find_one({"email": email})
    if user and check_password_hash(user["password"], password):
        token = create_token(user["_id"])
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
