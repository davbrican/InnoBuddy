import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import ratings_service

## Necesita popular después de ejecutar estas pruebas, afectan directamente al contenido de la base de datos
## Correrlas dos veces seguidas sin popular conlleva el fallo de varias pruebas en la segunda ejecución

def test_get_all_ratings():
    assert ratings_service.get_all_ratings()[0][1] == 0
    assert ratings_service.get_all_ratings()[0][2] == 0
    
def test_update_ratings_positivas():
    assert ratings_service.get_all_ratings()[0][1] == 0
    ratings_service.update_ratings("positiva")
    assert ratings_service.get_all_ratings()[0][1] == 1
    
def test_update_ratings_negativas():
    assert ratings_service.get_all_ratings()[0][2] == 0
    ratings_service.update_ratings("negativa")
    assert ratings_service.get_all_ratings()[0][2] == 1