from flask import Blueprint, request, jsonify
from app.auth.services import login_user

auth_bp = Blueprint("auth",__name__,url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    try:
        result = login_user(
            email=data.get("email"),
            password=data.get("password")
        )
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401