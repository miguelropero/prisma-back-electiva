
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, Numeric, String, DateTime
from sqlalchemy.ext.declarative import declarative_base  

base = declarative_base()

app = Flask(__name__)
ma = Marshmallow(app)

class User(base):  
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "password", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)