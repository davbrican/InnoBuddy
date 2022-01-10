import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/repositories")
import mongodb_repository

def get_all_data():
    return mongodb_repository.get_all_data()

def get_by_titulo(entrance):
    return mongodb_repository.get_by_titulo(entrance)

def get_by_day(entrance):
    return mongodb_repository.get_by_day(entrance)

def get_by_id(entrance):
    return mongodb_repository.get_by_id(entrance)