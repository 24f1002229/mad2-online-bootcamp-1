from flask import Flask, render_template, request, jsonify
from werkzeug import check_password, login_user
from backend.models import *
from app import app 

@app.route("/")
def home():
    return render_template("home.html")
