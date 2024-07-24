from config import Resource, db, app
from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager


app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JWT_TOKEN_LOCATION'] = ['headers']
jwt = JWTManager(app)