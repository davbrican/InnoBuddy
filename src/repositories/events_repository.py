import sys
import os
import inspect
from datetime import date, datetime
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/db")
import utils

def find_all_events():
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM eventos''')
        result = cursor.fetchall()
    return result

def find_event_by_day(dia):
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute(f'''
            SELECT * FROM eventos WHERE inicio BETWEEN '{dia} 00:00:00' AND '{dia} 23:59:59' ''')
        result = cursor.fetchall()
    return result

def find_event_by_day_today():
    hoy = datetime.now().strftime('%Y-%m-%d')
    conn = utils.connect()
    with conn.cursor() as cursor:
        cursor.execute(f'''
            SELECT * FROM eventos WHERE inicio BETWEEN '{hoy} 00:00:00' AND '{hoy} 23:59:59' ''')
        result = cursor.fetchall()
    return result