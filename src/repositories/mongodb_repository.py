from datetime import datetime
from utils import load_mongo
    
def get_all_data():
    collection = load_mongo()
    return collection.find()

def get_by_titulo(entrance):
    collection = load_mongo()
    return collection.find_one({"titulo": entrance})
    
def get_by_day(entrance):
    collection = load_mongo()
    end = datetime(entrance.year, entrance.month, entrance.day, 23, 0, 0)
    return collection.find({"inicio": {"$gte": entrance, "$lt": end}})