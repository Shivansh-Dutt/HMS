from flask import Blueprint, jsonify ,request
from flask_jwt_extended import jwt_required , get_jwt_identity
from app.auth.decorators import role_required
from app.doctor.services import get_upcoming_appointments
from app.doctor.services import get_assigned_patients
from app.doctor.services import update_appointment_status
from app.doctor.services import create_treatment
from app.doctor.services import get_patient_history
from app.doctor.services import update_doctor_availablity

doctor_bp = Blueprint("doctor",__name__, url_prefix="/doctor")

@doctor_bp.route("/dashboard",methods=["GET"])
@jwt_required()
@role_required("DOCTOR")
def dashboard():
    doctor_user_id = get_jwt_identity()
    return jsonify(get_upcoming_appointments(doctor_user_id))

@doctor_bp.route("/patients", methods=["GET"])
@jwt_required()
@role_required("DOCTOR")
def patients():
    user_id = get_jwt_identity()
    return jsonify(get_assigned_patients(user_id))

@doctor_bp.route("/appointments/<int:appintment_id>/status", methods=["PATCH"])
@jwt_required()
@role_required("DOCTOR")
def update_status(appointment_id):
    user_id = get_jwt_identity()
    return jsonify(update_appointment_status(user_id, appointment_id))

@doctor_bp.route("/appointments/<int:appointment_id>/treatment", methods=["POST"])
@jwt_required()
@role_required("DOCTOR")
def add_treatment(appointment_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    return jsonify(create_treatment(user_id, appointment_id, data)), 201

@doctor_bp.route("/patient/<int:patient_id>/history",methods=["GET"])
@jwt_required()
@role_required("DOCTOR")
def patient_history(patient_id):
    user_id = get_jwt_identity()
    return jsonify(get_patient_history(user_id, patient_id))

@doctor_bp.route("/availablity", methods=["PATCH"])
@jwt_required()
@role_required("DOCTOR")
def update_availablity():
    data = request.get_json()
    user_id = get_jwt_identity()
    return jsonify(update_doctor_availablity(user_id, data))