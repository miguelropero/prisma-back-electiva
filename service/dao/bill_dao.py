
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, Numeric, String, DateTime
from sqlalchemy.ext.declarative import declarative_base  

base = declarative_base()

app = Flask(__name__)
ma = Marshmallow(app)

class Bill(base):  
    __tablename__ = 'bill'

    id = Column(Integer, primary_key=True)
    date_bill = Column(DateTime)
    user_id = Column(Numeric)
    value = Column(Numeric)
    type = Column(Numeric)
    observation = Column(String)



class BillSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "user_id", "date_bill", "value", "type", "observation")

bill_schema = BillSchema()
bills_schema = BillSchema(many=True)