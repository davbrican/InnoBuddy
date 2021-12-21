import pymongo
import pprint

client = pymongo.MongoClient("mongodb+srv://usbicate:usbicate@innosofteventia.a1j4z.mongodb.net/innosoftEventia?retryWrites=true&w=majority")

'''
#EJEMPLO PARA IMPRIMIR TODOS LOS ENVENTOS DE LA BASE DE DATOS

db = client['innosoftEventia']

collection = db['peticionpublicacions']

pprint.pprint(collection.find_one({"titulo":"Lo que nadie me contó durante la universidad"}))
for entrada in collection.find():
    pprint.pprint(entrada)
'''