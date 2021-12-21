import pymongo
import pprint
import os
from dotenv import load_dotenv

load_dotenv()
client = pymongo.MongoClient(os.getenv('LINK_MONGO'))

'''
#EJEMPLO PARA IMPRIMIR TODOS LOS ENVENTOS DE LA BASE DE DATOS

db = client['innosoftEventia']

collection = db['peticionpublicacions']

pprint.pprint(collection.find_one({"titulo":"Lo que nadie me contó durante la universidad"}))
for entrada in collection.find():
    pprint.pprint(entrada)
'''