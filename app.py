from flask import Flask, jsonify, request
from service.dao.bill_dao import bill_schema, bills_schema
from service.dao.user_dao import user_schema
import service.bill_service as bill_service, service.user_service as user_service

app = Flask(__name__)

"""
- Metodo que devuelve un bill dado su identificador
- Params: id: identificador del bill
- Return objeto json asociado al id, vacio en caso de no encontrar coicidencias
"""
@app.route('/bill/<id>')
def get(id):
    bill = bill_service.get(id)
    return bill_schema.dump(bill)

"""
- Metodo que elimina un bill dado su identificador
- Params: id: identificador del bill a ser eliminado
- Return objeto json asociado al registro eliminado, vacio en caso de no encontrar coicidencias
"""
@app.route('/bill/<id>', methods=['DELETE'])
def delete(id):
    bill = bill_service.delete(id)
    return bill_schema.dump(bill)

"""
- Metodo que devuelve todos los bills registrados en la BD
- Return Lista de objetos json, vacio en caso de no encontrar registros
"""
@app.route('/bills/<username>')
def list(username):
    bills = bill_service.list(username)
    return jsonify(bills_schema.dump(bills))

"""
- Metodo que registra un nuevo bill
- Params: datos de creacion del bill: user_id, value, type, observation
- Return objeto json del registro creado, vacio en caso de error
"""
@app.route('/bill', methods=['POST'])
def save():

    request_data = request.get_json()
    user_id = request_data['user_id']
    value = request_data['value']
    type = request_data['type']
    observation = request_data['observation']

    bill = bill_service.save(user_id, value, type, observation)
    return bill_schema.dump(bill)

"""
- Metodo que permite validar las credenciales de autenticacion de usuario contra la tabla users
- Params: datos de autenticacion, usuario tipo string y password tipo string
- Return objeto json del usuario si las credenciales son validas, vacio en caso contrario 
"""
@app.route('/login', methods=['POST'])
def login():

    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    user = user_service.login(username, password)
    
    if(user):
        user.password = "*****"

    return user_schema.dump(user)

"""Documentando el metodo"""
@app.route('/login2', methods=['POST'])
def login2():

    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    user = user_service.login(username, password)
    
    if(user):
        user.password = "*****"

    return user_schema.dump(user)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

# sudo apt-get install -y python3-pip
# sudo apt install libpq-dev python3-dev
# export PATH=${PATH}:/usr/bin/python3
# python3 -m venv my_env
# source my_env/bin/activate

# pip3 install psycopg2
# pip install flask-marshmallow
# pip install flask flask-jsonpify flask-sqlalchemy flask-restful


# export FLASK_APP=bill_controller
# export FLASK_ENV=development
# flask run
