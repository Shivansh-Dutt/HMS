from flask import Blueprint,request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.auth.decorators import role_required
from app.patient.services import register_patient
from app.patient.services import get_patient_dashboard
from app.patient.services import search_available_doctors
from app.patient.services import book_appointment,cancel_appointment,get_patient_history,export_history_of_patient
from app.services.department_service import get_department
from app.services.doctor_service import get_department_doctors

patient_bp = Blueprint("patient",__name__, url_prefix="/patient")

@patient_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return jsonify(register_patient(data))

@patient_bp.route("/dashboard", methods=["GET"])
@jwt_required()
@role_required("PATIENT")
def dashboard():
    user_id = get_jwt_identity()
    return jsonify(get_patient_dashboard(user_id))

@patient_bp.route("/department/<int:id>", methods=["GET"])
@jwt_required()
@role_required("PATIENT")
def department_details(id):
    return jsonify({
        "department_detail" : get_department(id),
        "department_doctors"  : get_department_doctors(id)
        })

@patient_bp.route("/doctors/search", methods=["GET"])
@jwt_required()
@role_required("PATIENT")
def search_doctors():
    query = request.args.get("q", "")
    return jsonify(search_available_doctors(query))

@patient_bp.route("/appointments", methods=["POST"])
@jwt_required()
@role_required("PATIENT")
def book():
    data = request.get_json()
    user_id = get_jwt_identity()
    return jsonify(book_appointment(user_id, data)), 201

@patient_bp.route("/appointments/<int:appointment_id>/cancel", methods=["PATCH"])
@jwt_required()
@role_required("PATIENT")
def cancel(appointment_id):
    user_id = get_jwt_identity()
    return jsonify(cancel_appointment(user_id, appointment_id))

@patient_bp.route("/history", methods=["GET"])
@jwt_required()
@role_required("PATIENT")
def history():
    user_id = get_jwt_identity()
    return jsonify(get_patient_history(user_id))


@patient_bp.route("/export", methods=["POST"])
@jwt_required()
@role_required("PATIENT")
def export_history():
    user_id = get_jwt_identity()
    return jsonify(export_history_of_patient(user_id))