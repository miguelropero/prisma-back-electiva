Miguel Ropero
Prueba técnica backend / Prisma


###########################################
#### Preparación del entorno de trabajo ###
###########################################
Librerías necesarias para ejecutar el proyecto: 

Python versión 3.9+

Otras librerías: 

sudo apt-get install libpq-dev python-dev-is-python3
sudo apt install python3-pip
udo apt install python3-flask

pip3 install psycopg2
pip install flask-marshmallow
pip install flask flask-jsonpify flask-sqlalchemy flask-restful

###########################################
######## Ejecución de la aplicación #######
###########################################

python3 app.py

###########################################
###### Arquitectura de la aplicación ######
###########################################

La aplicación esta construida sobre un modelo de capas: 

CAPA Controller: 
Expone los servicios web que responde la aplicación: 


Servicios de Bill: 
get(id): Retorna un bill dado su id
GET http://ec2-54-242-183-194.compute-1.amazonaws.com:5000/bill/4

delete(id): ELimina un bill dado su id
DELETE http://ec2-54-242-183-194.compute-1.amazonaws.com:5000/bill/4

list(): Lista todos los registros de la tabla bill de un usuario
GET http://ec2-54-242-183-194.compute-1.amazonaws.com:5000/bills

save(): Registra un nuevo bill
POST http://ec2-54-242-183-194.compute-1.amazonaws.com:5000/bill

{
    "user_id": 1,
    "value": 1000,
    "type": 1,
    "observation": "Postman"
}

login(): valida si las credenciales ingresadas por un usuario sin validas
POST http://ec2-54-242-183-194.compute-1.amazonaws.com:5000/login

{
    "username": "cramirez",
    "password": "Prisma22"
}

---------------------------------------------------------------------
CAPA Negocio
Ubicada dentro del directorio DAO. COntiene la lógica de negocio que 
permite procesar las solicitudes recibidas por la capa controller. 

---------------------------------------------------------------------
CAPA Persistencia
Gestiona las conexiones de BD y atiende las diferentes operaciones CRUD
solicitadas por la capa de negocio

###########################################
############# Librerías Usadas ############
###########################################

Flask: Exposición de servicios web
sqlalchemy: ORM, gestión de conexiones y operaciones sobre la BD
Marshmallow: Serialización de objetos


 


