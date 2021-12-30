import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/repositories")
import localizaciones_repository

def find_localizacion_by_aula(aula):
    return localizaciones_repository.find_localizacion_by_aula(aula)