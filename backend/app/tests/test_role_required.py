import pytest 
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from app.auth.decorators import role_required

@pytest.fixture
def app():
    app = Flask(__name__)
    
    app.config["TESTING"] = True
    app.config["JWT_SECRET_KEY"] = "test-secret"
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_HEADER_NAME"] = "Authorization"
    app.config["JWT_HEADER_TYPE"] = "Bearer"
    
    JWTManager(app)

    @app.route("/admin-only")
    @role_required("admin")
    def admin_only():
        return jsonify({"msg": "success"}), 200

    return app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def make_token(app):
    def _make_token(role):
        with app.app_context():
            return create_access_token(
                identity=str(1),
                additional_claims={"role": role}
            )
    return _make_token

def test_admin_access_allowed(client, make_token):
    token = make_token("admin")

    response = client.get(
        "/admin-only",
        headers={"Authorization": f"Bearer {token}"}
    )

    print("STATUS:", response.status_code)
    print("JSON:", response.get_json())

    assert response.status_code == 200

def test_access_deined_for_wrong_role(client, make_token):
    token = make_token("doctor")
    
    response = client.get(
        "/admin-only",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 403
    assert response.json["error"] == "Access denied"
    
def test_missing_token(client):
    response = client.get("/admin-only")

    assert response.status_code == 401
