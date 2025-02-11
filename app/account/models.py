from app.app import db
from datetime import datetime
from flask_login import UserMixin



class RegistrationModel(UserMixin, db.Model):

    __tablename__ = 'registration'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(10), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now) 
    # parent relation
    # one to one relationship
    profile_info = db.relationship('ProfileSetupModel', backref='registration', uselist=False)

    def __repr__(self):
        return self.username
    
    def get_id(self):
        return self.uid
    
