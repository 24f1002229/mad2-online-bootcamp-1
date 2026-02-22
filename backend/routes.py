from flask import Flask,render_template, request, jsonify
from werkzeug.security import check_password_hash,generate_password_hash
from flask_security import login_user, auth_required, roles_required
from flask_login import current_user
from .utils import roles_list
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
    
    user = app.security.datastore.find_user(email = email)
    
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            print(current_user)
            return jsonify({
                "id"  : user.id,
                "username" : user.username,
                "auth-token" : user.get_auth_token(),
                "roles" : roles_list(current_user.roles) 
            })
        else:
            return jsonify({
                "message" : "Incorrect Password"
            })
        
    else:
        return jsonify({
            "message": "User not found !!"
        })


@app.route('/api/register', methods=['POST'])
def register():
    credentials = request.get_json()
    if not app.security.datastore.find_user(email = credentials["email"]):
        app.security.datastore.create_user(email = credentials["email"],
                                           username = credentials["username"],
                                           password = generate_password_hash(credentials["password"]),
                                           roles = ['user'])
        db.session.commit()
        return jsonify({
            "message" : "User Created Successfully !!"
        })
    return jsonify({
        "message": "User Already Exists !!"
    })

@app.route("/api/admin")
@auth_required('token')
@roles_required('admin')
def admin():
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "roles": roles_list(current_user.roles)
    })


@app.route("/api/lot/<int:lot_id>", methods=["GET"])
@auth_required("token")
@roles_required("admin")
def get_lot(lot_id):
    lot = ParkingLot.query.get(lot_id)
    if not lot :
        return {"message" : "Lot is not exists"}
    
    return {
        "id" : lot_id,
        "prime_location_name" : lot.prime_location_name,
        "address" : lot.address,
        "pincode" : lot.pincode,
        "price" : lot.price,
        "spots" : [
            {
                "id": s.id,
                "is_occupied" : s.is_occupied
            } for s in lot.spots
        ]
    }
