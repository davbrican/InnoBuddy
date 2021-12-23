import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/repositories")
import start_repository

def find_user_by_id(id):
    return start_repository.find_user_by_id(id)

def add_user(id):
    return start_repository.add_user(id)

def add_user_if_new(id):
    user = find_user_by_id(id)
    if user == None:
        add_user(id)
    else:
        pass
        

