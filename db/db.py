from sqlalchemy import create_engine  
from sqlalchemy import Column, Integer, Numeric, String, DateTime  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://postgres:Prisma2022@prismatest.cr5kiddvokid.us-east-2.rds.amazonaws.com:5432/test"

db = create_engine(db_string)  
base = declarative_base()

Session = sessionmaker(db)  
session = Session()

# Save registre
def save(self):
    session.add(self)  
    session.commit()
    return self

# Get One
def get(self, id):
    return session.query(self).filter_by(id = id).first()

# Get all
def list(self, userId):
    #return session.query(self).all()
    return session.query(self).filter_by(user_id = userId).all()

# Delete
def delete(self):
    session.delete(self)  
    session.commit()

def login(self, username, password):
    return session.query(self).filter_by(username = username, password = password).first()

def getUserByUsername(self, username):
    return session.query(self).filter_by(username = username).first()
