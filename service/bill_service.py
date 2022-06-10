
from service.dao.bill_dao import Bill
from service.dao.user_dao import User

import service.user_service as user_service
import db.db as db
import datetime

current_time = datetime.datetime.now()

def save(user_id, value, type, observation):
    try:
        object = Bill(user_id=user_id, date_bill = current_time, value = value, type = type, observation = observation)  
        new = db.save(object)
        return new
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)


def list(username):
    try:
        user = user_service.getByUsername(username)

        if(user):
            list = db.list(Bill, user.id)
            return list
        return None
    except Exception as e:
        print("Ocurrió un error al consultar: ", e)

def get(id):
    object = db.get(Bill, id)
    return object

def delete(id):
    try:
        object = get(id)
        db.delete(object)
        return object
    except Exception as e:
        print("Ocurrió un error al eliminar: ", e)


