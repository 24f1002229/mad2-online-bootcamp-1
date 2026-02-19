from flask import Flask, render_template, request, jsonify
from werkzeug import check_password, login_user
from backend.models import *
from app import app 

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/login", methods=["POST"])
def user_login():
    body = request.get_json()
    email = body['email']
    password = body['password']

    if not email:
        return jsonify({
            "message" : "Email is required !"
        })
          

    if not password:
        return jsonify({
            "message" : "Password required !!"
        })
    
    user = app.security.datastore.find_user(email = email)
    
    if user:
        if check_password(user.password, password):
            login_user(user)
            print("current_user")
            return jsonify({
                "id"  : user.id,
                "username" : user.username,
                "auth-token" : user.get_auth_token(),
                "roles" : roles_list(current_user.roles) 
            })
