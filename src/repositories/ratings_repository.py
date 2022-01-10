import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/db")
from utils import connect


def get_all_ratings():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM valoraciones''')
    
    data = [i for i in cursor]
    conn.commit()
    cursor.close()
    conn.close()    
    return data



def update_ratings(tipo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM valoraciones''')
    
    data = [i for i in cursor]
    
    positivas = data[0][1]
    negativas = data[0][2]
    
    str_update = ""
    if tipo == "negativa":        
        negativas += 1
        str_update = '''UPDATE valoraciones SET negativas = {neg_n} WHERE id = 0;'''.format(neg_n = negativas)
    elif tipo == "positiva":
        positivas += 1
        str_update = '''UPDATE valoraciones SET positivas = {pos_n} WHERE id = 0;'''.format(pos_n = positivas)
        
    cursor.execute(str_update)
    conn.commit()
    cursor.close()
    conn.close()    
