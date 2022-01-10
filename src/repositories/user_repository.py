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

def find_all_users():
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM usuarios''')
        result = cursor.fetchall()
    return result

def add_user(id):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
        INSERT usuarios(id,rol) VALUES(%(id)s,"alumno")
        ''', {'id': id})
    conn.commit()

def find_user_by_id_and_rol(id,rol):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
        SELECT COUNT(*) FROM usuarios WHERE id = %(id)s AND rol = %(rol)s
        ''', {'id': id,'rol': rol})
        result = cursor.fetchone()
    return result[0]

def upgrade_user(id):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
        UPDATE usuarios SET rol = "admin" WHERE id = %(id)s
        ''', {'id': id})
    conn.commit()


def get_recordatorios(user_id):
    conn = utils.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `recordatorios` WHERE id_usuario LIKE "+str(user_id)+";")
    data = list(set([i for i in cursor]))
    cursor.close()
    conn.close()    
    
    return data

def insert_recordatorios(user_id, evento_id):
    conn = utils.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recordatorios VALUES("+str(user_id)+","+str(evento_id)+");")
    conn.commit()
    cursor.close()
    conn.close()    