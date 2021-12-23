import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/db")
import utils

def find_user_by_id(id):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM usuarios WHERE id = %(id)s
            ''', {'id': id})
        result = cursor.fetchone()
    return result

def add_user(id):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
        INSERT usuarios(id,rol) VALUES(%(id)s,"alumno")
        ''', {'id': id})
    conn.commit()
