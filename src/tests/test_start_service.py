import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import start_service

## Necesita popular después de ejecutar estas pruebas, afectan directamente al contenido de la base de datos
## Correrlas dos veces seguidas sin popular conlleva el fallo de varias pruebas en la segunda ejecución

def test_find_user_by_id():
    assert start_service.find_user_by_id(267547511) == (267547511,'alumno')

def test_find_all_users():
    assert start_service.find_all_users() == [(207767757, 'admin'), (267547511, 'alumno'), (686981968, 'alumno')]

def test_add_user():
    assert start_service.find_user_by_id(123456789) == None
    start_service.add_user(123456789)
    assert start_service.find_user_by_id(123456789) == (123456789,'alumno')

def test_add_user_if_new():
    assert start_service.find_user_by_id(123456788) == None
    start_service.add_user_if_new(123456788)
    assert start_service.find_user_by_id(123456788) == (123456788,'alumno')

def test_is_admin_true():
    assert start_service.is_admin(207767757) == True

def test_is_admin_false():
    assert start_service.is_admin(267547511) == False

def test_upgrade_user():
    assert start_service.find_user_by_id(267547511)[1] == 'alumno'
    start_service.upgrade_user(267547511)
    assert start_service.find_user_by_id(267547511)[1] == 'admin'
    
def test_get_recordatorios():
    assert start_service.get_recordatorios("483048011")[0][1] == "206188845387"