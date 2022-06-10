
from service.dao.user_dao import User
import db.db as db

def login(username, password):
    try:
        user = db.login(User, username, password)
        return user
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)

def getByUsername(username):
    try:
        user = db.getUserByUsername(User, username)
        return user
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)
