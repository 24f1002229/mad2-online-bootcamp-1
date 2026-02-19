from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    reminder_time = db.Column(db.Time(30), nullable=True)
    password = db.Column(db.String(30), nullable=False)
    fs_uniquifier = db.Column(db.String, unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    roles = db.relationship('Role', backref='bearer', secondary = 'users_roles')
    reservations = db.relationship('Reservation', back_populates='user')

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String)

class UsersRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class ParkingLot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prime_location_name = db.Column(db.String, nullable = False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String, nullable=False)
    pincode = db.Column(db.String, nullable=False)
    number_of_spots = db.Column(db.Integer, nullable=False)
    spots = db.relationship('ParkingSpot', backref='lot', cascade='all, delete-orphan')


class ParkingSpot(db.Model):
    id = db.Column(db.Float, primary_key=True)
    is_occupied = db.Column(db.Boolean, default = False)
    lot_id = db.Column(db.Integer, db.ForeignKey('parking_lot.id'), nullable=False)
    reservations = db.relationship('Reservation', back_populates='spot', cascade='all, delete-orphan')


class Reservation(db.Model):
    id = db.Column(db.Float, primary_key=True)
    parking_timestamp = db.Column(db.DateTime, default=None)
    leaving_timestamp = db.Column(db.DateTime, default= None)
    parking_cost = db.Column(db.Float, nullable=False)
    vehicle_number = db.Column(db.String, nullable=False)
    remarks = db.Column(db.String)
    spot_id = db.Column(db.Integer, db.ForeignKey('parking_spot.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') ,nullable=False)
    user = db.relationship('User', back_populates='reservations')
    spot = db.relationship('ParkingSpot', back_populates='reservations')