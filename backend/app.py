from flask import Flask, request, jsonify
import jwt
from functools import wraps
from config import SECRET_KEY
from email_service import fetch_emails
from auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing!"}), 403
        try:
            jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({"error": "Invalid token!"}), 403
        return f(*args, **kwargs)
    return decorated

@app.route("/fetch_emails", methods=["POST"])
@token_required
def get_emails():
    data = request.json
    user_email, app_password = data.get("email"), data.get("password")
    emails = fetch_emails(user_email, app_password)
    return jsonify(emails), 200  


if __name__ == "__main__":
    app.run(debug=True)
