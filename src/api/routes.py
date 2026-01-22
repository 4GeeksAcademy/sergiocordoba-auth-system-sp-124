"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from models import User, db

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/sign_in', methods=['POST', 'GET'])
def handle_sign_in():

    response_body = {
        "message": "Crear Usuario"
    }

    return jsonify(response_body), 200


@api.route('/login', methods=['GET'])
def handle_login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)    

    User = db.session.execute(db.select('User').where(User.password == password, User.email == email, User.is_active))


    response_body = {
        "message": "Iniciar sesión"
    }

    return jsonify(response_body), 200

