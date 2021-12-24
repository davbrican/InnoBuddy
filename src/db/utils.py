import mysql.connector
import os
from dotenv import load_dotenv
import pymongo
import ssl

load_dotenv()

def connect():
    conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASS"),
    database=os.getenv("MYSQL_DB")
    )
    return conn

def load_mongo():
    client = pymongo.MongoClient(os.getenv('LINK_MONGO'), ssl_cert_reqs=ssl.CERT_NONE)

    #EJEMPLO PARA IMPRIMIR TODOS LOS ENVENTOS DE LA BASE DE DATOS
    db = client['innosoftEventia']
    collection = db['peticionpublicacions']
    
    return collection