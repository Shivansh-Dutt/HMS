from flask import Blueprint, request, jsonify
from app.auth.services import login_user
from flask_jwt_extended import set_access_cookies,jwt_required, get_jwt,get_jwt_identity
from app.models import User
auth_bp = Blueprint("auth",__name__,url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    try:
        result = login_user(
            email=data.get("email"),
            password=data.get("password")
        )
        # return jsonify(result), 200
         # Set JWT in HttpOnly cookie
        resp = jsonify({
            "email": result["email"],
            "role": result["role"]
        })
        set_access_cookies(resp, result["access_token"])

        return resp, 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    
@auth_bp.route("/me",methods=["GET"])
@jwt_required()
def me():
    claims = get_jwt()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        "authenticated": True,
        "role": claims.get("role"),
        "email": user.email
    }), 200