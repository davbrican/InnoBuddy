import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import localizaciones_service

def test_find_localizacion_by_aula():
    assert localizaciones_service.find_localizacion_by_aula("A0.11") == ("A0.11", 386, 495)