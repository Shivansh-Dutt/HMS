from flask import Blueprint,request , jsonify
from flask_jwt_extended import jwt_required
from app.auth.decorators import role_required
from app.admin.services import (
    dashboard_stats,
    create_doctor,
    search_doctors,
    search_patients,
    disable_user
)

admin_bp  = Blueprint("admin",__name__,url_prefix="/admin")

@admin_bp.route("/dashboard",methods=["GET"])
@jwt_required()
@role_required("ADMIN")
def dashboard():
    return jsonify(dashboard_stats())

@admin_bp.route("/doctors", methods=["POST"])
@jwt_required()
@role_required("ADMIN")
def add_doctor():
    data = request.get_json()
    return jsonify(create_doctor(data)), 201

@admin_bp.route("/doctors/search",methods=["GET"])
@jwt_required()
@role_required("ADMIN")
def search_doctor():
    query = request.args.get("q", "")
    return jsonify(search_doctor(query))

@admin_bp.route("/patients/search", methods=["GET"])
@jwt_required()
@role_required("ADMIN")
def search_patient():
    query = request.args.get("q","")
    return jsonify(search_patients(query))

@admin_bp.route("/users/<int:user_id>/disable", methods=["PATCH"])
@jwt_required()
@role_required("ADMIN")
def disable(user_id):
    return jsonify(disable_user(user_id))