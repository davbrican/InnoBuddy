import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/db")
import utils

def find_localizacion_by_aula(aula):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM localizaciones WHERE aula = %(aula)s
            ''', {'aula': aula})
        result = cursor.fetchone()
    return result
