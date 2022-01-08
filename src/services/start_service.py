import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/repositories")
import start_repository

def find_user_by_id(id):
    return start_repository.find_user_by_id(id)

def find_all_users():
    return start_repository.find_all_users()

def add_user(id):
    return start_repository.add_user(id)

def add_user_if_new(id):
    user = find_user_by_id(id)
    if user == None:
        add_user(id)
    else:
        pass

def is_admin(id):
    if start_repository.find_user_by_id_and_rol(id,'admin')==1:
        return True
    else:
        return False

def upgrade_user(id):
    return start_repository.upgrade_user(id)

def get_recordatorios(user_id):
    return start_repository.get_recordatorios(user_id)