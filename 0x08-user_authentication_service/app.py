#!/usr/bin/env python3
"""FLASK module"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """index"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """users"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route('/sessions', methods=['POST'])
def login():
    """Login method"""
    email = request.form.get('email')
    password = request.form.get('password')
    valid_login = AUTH.valid_login(email, password)

    if valid_login:
        session_id = AUTH.create_session(email)
        msg = {"email": "<user email>", "message": "logged in"}
        response = jsonify(msg)
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")